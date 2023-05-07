from typing import List

import tiktoken

OPENAI_MODEL_FINE_TUNING_PRICING = {
    "ada": 0.0004,
    "curie": 0.0006,
    "babbage": 0.0030,
    "davinci": 0.0300
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


def estimate_costs_fine_tune(train_data: List[str], openai_model: str, n_epochs: int = 5) -> float:
    # TODO: ESTIMATE OPENAI FINE TUNE COSTS
    return 0.0
