import logging
from collections import defaultdict

import evaluate
import numpy as np
from transformers import AutoTokenizer
from tqdm.auto import tqdm


SQUAD = evaluate.load("squad")
METEOR = evaluate.load("meteor")
BLEU = evaluate.load("bleu")
BERTSCORE = evaluate.load("bertscore")


# MODEL_CHECKPOINT = "distilbert-base-uncased-distilled-squad"
MODEL_CHECKPOINT = "deepset/deberta-v3-base-squad2"
MAX_LEN = 384
STRIDE = 128

TOKENIZER = AutoTokenizer.from_pretrained(MODEL_CHECKPOINT)


logging.getLogger(__name__).addHandler(logging.NullHandler())


def preprocess_training(examples):
    questions = [q.strip() for q in examples["question"]]
    inputs = TOKENIZER(
        questions,
        examples["context"],
        max_length=MAX_LEN,
        truncation="only_second",
        stride=STRIDE,
        return_overflowing_tokens=True,
        return_offsets_mapping=True,
        padding="max_length",
    )

    offset_mapping = inputs.pop("offset_mapping")
    sample_map = inputs.pop("overflow_to_sample_mapping")
    answers = examples["answers"]
    start_positions = []
    end_positions = []

    for i, offset in enumerate(offset_mapping):
        sample_idx = sample_map[i]
        answer = answers[sample_idx]
        start_char = answer["answer_start"][0]
        end_char = answer["answer_start"][0] + len(answer["text"][0])
        sequence_ids = inputs.sequence_ids(i)

        idx = 0
        while sequence_ids[idx] != 1:
            idx += 1
        context_start = idx
        while sequence_ids[idx] == 1:
            idx += 1
        context_end = idx - 1

        if offset[context_start][0] > start_char or offset[context_end][1] < end_char:
            start_positions.append(0)
            end_positions.append(0)
        else:
            idx = context_start
            while idx <= context_end and offset[idx][0] <= start_char:
                idx += 1
            start_positions.append(idx - 1)

            idx = context_end
            while idx >= context_start and offset[idx][1] >= end_char:
                idx -= 1
            end_positions.append(idx + 1)

    inputs["start_positions"] = start_positions
    inputs["end_positions"] = end_positions
    return inputs


def preprocess_validation(examples):
    questions = [q.strip() for q in examples["question"]]
    inputs = TOKENIZER(
        questions,
        examples["context"],
        max_length=MAX_LEN,
        truncation="only_second",
        stride=STRIDE,
        return_overflowing_tokens=True,
        return_offsets_mapping=True,
        padding="max_length",
    )

    sample_map = inputs.pop("overflow_to_sample_mapping")
    example_ids = []

    for i in range(len(inputs["input_ids"])):
        sample_idx = sample_map[i]
        example_ids.append(examples["id"][sample_idx])

        sequence_ids = inputs.sequence_ids(i)
        offset = inputs["offset_mapping"][i]
        inputs["offset_mapping"][i] = [
            o if sequence_ids[k] == 1 else None for k, o in enumerate(offset)
        ]

    inputs["example_id"] = example_ids
    return inputs


def compute_metrics(start_logits, end_logits, features, examples):
    example_to_features = defaultdict(list)
    for idx, feature in enumerate(features):
        example_to_features[feature["example_id"]].append(idx)

    predicted_answers = []
    for example in tqdm(examples):
        example_id = example["id"]
        context = example["context"]
        answers = []

        for feature_index in example_to_features[example_id]:
            start_logit = start_logits[feature_index]
            end_logit = end_logits[feature_index]
            offsets = features[feature_index]["offset_mapping"]

            start_indexes = np.argsort(start_logit)[-1: -20 - 1: -1].tolist()
            end_indexes = np.argsort(end_logit)[-1: -20 - 1: -1].tolist()
            for start_index in start_indexes:
                for end_index in end_indexes:
                    if offsets[start_index] is None or offsets[end_index] is None:
                        continue
                    if (
                        end_index < start_index
                        or end_index - start_index + 1 > 30
                    ):
                        continue

                    answer = {
                        "text": context[offsets[start_index][0]: offsets[end_index][1]],
                        "logit_score": start_logit[start_index] + end_logit[end_index],
                    }
                    answers.append(answer)

        if len(answers) > 0:
            best_answer = max(answers, key=lambda x: x["logit_score"])
            predicted_answers.append(
                {"id": example_id, "prediction_text": best_answer["text"]}
            )
        else:
            predicted_answers.append({"id": example_id, "prediction_text": ""})

    theoretical_answers = [
        {"id": ex["id"], "answers": ex["answers"]} for ex in examples]

    p_answers = [predicted["prediction_text"]
                 for predicted in predicted_answers]
    t_answers = [expected["answers"]["text"][0]
                 for expected in theoretical_answers]

    return {
        "SQUAD": SQUAD.compute(predictions=predicted_answers, references=theoretical_answers),
        "Meteor": METEOR.compute(predictions=p_answers, references=t_answers),
        "BLEU-4": BLEU.compute(predictions=p_answers, references=t_answers),
        "BERTscore": BERTSCORE.compute(predictions=p_answers, references=t_answers, lang="en", model_type="microsoft/deberta-base")
    }
