import logging
from typing import List

import jsonlines
import tiktoken

logging.getLogger(__name__).addHandler(logging.NullHandler())

OPENAI_MODEL_FINE_TUNING_TRAINING_PRICING = {
    "ada": 0.0004,
    "curie": 0.0006,
    "babbage": 0.0030,
    "davinci": 0.0300
}

OPENAI_MODEL_FINE_TUNING_USAGE_PRICING = {
    "ada": 0.0016,
    "curie": 0.0024,
    "babbage": 0.0120,
    "davinci": 0.1200
}


def count_tokens(text: str, openai_model: str = "ada") -> int:
    encoding = tiktoken.encoding_for_model(openai_model)
    return len(encoding.encode(text))


def encode_tokens(text: str, openai_model: str = "ada") -> int:
    encoding = tiktoken.encoding_for_model(openai_model)
    return encoding.encode(text)


def decode_tokens(tokens: List[int], openai_model: str = "ada") -> int:
    encoding = tiktoken.encoding_for_model(openai_model)
    return encoding.decode(tokens)


def estimate_costs_fine_tune_training(train_data: List[str], openai_model: str, n_epochs: int = 5) -> float:
    n_tokens = 0
    with jsonlines.open(train_data, "r") as reader:
        for line in reader:
            n_tokens += count_tokens(line["prompt"])
            n_tokens += count_tokens(line["completion"])
    n_tokens *= n_epochs
    tokens_per_1k = n_tokens/1000
    return tokens_per_1k * OPENAI_MODEL_FINE_TUNING_TRAINING_PRICING[openai_model]


def estimate_costs_fine_tune_usage(test_data: List[str], openai_model: str) -> float:
    n_tokens = 0
    with jsonlines.open(test_data, "r") as reader:
        for line in reader:
            n_tokens += count_tokens(line["prompt"])
    tokens_per_1k = n_tokens/1000
    return tokens_per_1k * OPENAI_MODEL_FINE_TUNING_USAGE_PRICING[openai_model]
