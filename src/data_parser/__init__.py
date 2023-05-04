import logging
import jsonlines
from random import random
from typing import List

import utils

logging.getLogger(__name__).addHandler(logging.NullHandler())

MAX_TOKENS = 2048 - 128 
END_OF_PROMPT = "\n\n###\n\n"


def __prepare_prompt(clickbait: List[str], article: List[str]) -> str:
    clickbait = "\n".join(clickbait)
    article = "\n".join(article)
    prompt = f"CLICKBAIT:\n\n{clickbait}\n\n\nARTICLE:\n\n{article}"

    if utils.count_tokens(prompt) >= MAX_TOKENS:
        limit = MAX_TOKENS - utils.count_tokens(END_OF_PROMPT)
        prompt_encoded = utils.encode_tokens(prompt)
        prompt_encoded = prompt_encoded[:limit]
        prompt = utils.decode_tokens(prompt_encoded)

    return f"{prompt}{END_OF_PROMPT}"


def __prepare_completion(spoiler: List[str]) -> str:
    spoiler = "\n".join(spoiler)
    return f" {spoiler} END"


def prepare_data_to_fine_tune(input_path: str, output_path: str) -> None:
    with jsonlines.open(input_path, "r") as reader:
        with jsonlines.open(output_path, "w") as writer:
            for line in reader:
                prompt = __prepare_prompt(
                    line["postText"],
                    line["targetParagraphs"]
                )
                completion = __prepare_completion(line["spoiler"])

                writer.write({
                    "prompt": prompt,
                    "completion": completion
                })


def prepare_data_test(input_path: str, output_test_path: str, output_validation_path: str, test_size: float = 0.75) -> None:
    with jsonlines.open(input_path, "r") as reader:
        with jsonlines.open(output_test_path, "w") as test_writer:
            with jsonlines.open(output_validation_path, "w") as val_writer:
                for line in reader:
                    prompt = __prepare_prompt(
                        line["postText"],
                        line["targetParagraphs"]
                    )
                    completion = __prepare_completion(line["spoiler"])
                    if random() > test_size:
                        val_writer.write({
                            "prompt": prompt,
                            "completion": completion
                        })
                    else:
                        test_writer.write({
                            "prompt": prompt,
                            "completion": completion
                        })
