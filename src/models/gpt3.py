import logging
import time
from typing import List, Dict

import openai
import jsonlines

from data_parser import OPENAI_END_OF_COMPLETION, OPENAI_MAX_TOKENS_COMPLETION

logging.getLogger(__name__).addHandler(logging.NullHandler())

TEMPERATURE = 0.07
MAX_TOKENS = OPENAI_MAX_TOKENS_COMPLETION
PRESENCE_PENALTY = 0.0
FREQUENCY_PENALY = 0.0
STOP = [OPENAI_END_OF_COMPLETION]


def read_data(dataset_path: str) -> List[Dict[str, str]]:
    data = []
    with jsonlines.open(dataset_path, "r") as reader:
        for line in reader:
            data.append({
                "id": line["id"],
                "type": line["type"],
                "prompt": line["prompt"],
                "completion": line["completion"].replace(STOP[0], "").strip()
            })
    return data


def _predict(clickbait: str, model_id: str) -> str:
    results = openai.Completion.create(
        prompt=clickbait,
        model=model_id,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        presence_penalty=PRESENCE_PENALTY,
        frequency_penalty=FREQUENCY_PENALY,
        stop=STOP
    )
    return [result.text.strip() for result in results.choices]


def predict(prompts: str, model_id: str, sleep_time: float = 1.0) -> List[str]:
    predictions = []
    for prompt in prompts:
        predictions.append(_predict(prompt, model_id))
        time.sleep(sleep_time)
    return predictions
