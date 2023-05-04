from typing import List

import tiktoken

GPT_TOKENIZER = "r50k_base"


def count_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding(GPT_TOKENIZER)
    return len(encoding.encode(text))


def encode_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding(GPT_TOKENIZER)
    return encoding.encode(text)


def decode_tokens(tokens: List[int]) -> int:
    encoding = tiktoken.get_encoding(GPT_TOKENIZER)
    return encoding.decode(tokens)
