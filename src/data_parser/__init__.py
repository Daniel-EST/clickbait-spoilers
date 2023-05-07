import logging
import jsonlines
import random
from typing import List

import utils.openai as openai

logging.getLogger(__name__).addHandler(logging.NullHandler())

OPENAI_MAX_TOKENS_COMPLETION = 128
OPENAI_MAX_TOKENS_PROMPT = 2048 - OPENAI_MAX_TOKENS_COMPLETION
OPENAI_END_OF_PROMPT = "\n\n###\n\n"
OPENAI_END_OF_COMPLETION = " END"


def __prepare_prompt_openai(clickbait: List[str], article: List[str], openai_model: str) -> str:
    clickbait = "\n".join(clickbait)
    article = "\n".join(article)
    prompt = f"CLICKBAIT:\n\n{clickbait}\n\n\nARTICLE:\n\n{article}"

    if openai.count_tokens(prompt, openai_model) >= OPENAI_MAX_TOKENS_PROMPT:
        limit = OPENAI_MAX_TOKENS_PROMPT - \
            openai.count_tokens(OPENAI_END_OF_PROMPT, openai_model)
        prompt_encoded = openai.encode_tokens(prompt, openai_model)
        prompt_encoded = prompt_encoded[:limit]
        prompt = openai.decode_tokens(prompt_encoded, openai_model)
    return f"{prompt}{OPENAI_END_OF_PROMPT}"


def __prepare_completion_openai(spoiler: List[str], openai_model: str) -> str:
    spoiler = "\n".join(spoiler)
    if openai.count_tokens(spoiler, openai_model) >= OPENAI_MAX_TOKENS_COMPLETION:
        limit = OPENAI_MAX_TOKENS_COMPLETION - \
            openai.count_tokens(OPENAI_END_OF_COMPLETION, openai_model)
        spoiler_encoded = openai.encode_tokens(spoiler, openai_model)
        spoiler_encoded = spoiler_encoded[:limit]
        spoiler = openai.decode_tokens(spoiler_encoded, openai_model)
    return f" {spoiler}{OPENAI_END_OF_COMPLETION}"


def prepare_data_to_fine_tune_openai(input_path: str, output_path: str, openai_model: str) -> None:
    with jsonlines.open(input_path, "r") as reader:
        with jsonlines.open(output_path, "w") as writer:
            for line in reader:
                prompt = __prepare_prompt_openai(
                    line["postText"],
                    line["targetParagraphs"],
                    openai_model
                )
                completion = __prepare_completion_openai(
                    line["spoiler"], openai_model)
                writer.write({
                    "prompt": prompt,
                    "completion": completion
                })


def prepare_data_to_fine_tune_bert(input_path: str, output_path: str) -> None:
    with jsonlines.open(input_path, "r") as reader:
        with jsonlines.open(output_path, "w") as writer:
            for line in reader:
                writer.write({
                    "clickbait": "\n".join(line["postText"]),
                    "text": "\n".join(line["targetParagraphs"]),
                    "spoiler": "\n".join(line["spoiler"])
                })


def prepare_split_data(input_path: str, output_folder: str, split_size: float = 0.75) -> None:
    output_test_path = f"{output_folder}/test.jsonl"
    output_val_path = f"{output_folder}/validation.jsonl"
    with jsonlines.open(input_path, "r") as reader:
        with jsonlines.open(output_test_path, "w") as test_writer:
            with jsonlines.open(output_val_path, "w") as val_writer:
                for line in reader:
                    if random.random() < split_size:
                        test_writer.write(line)
                    else:
                        val_writer.write(line)
