import logging
import argparse

import data_parser

logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)

OPENAI_MODEL = "ada"


def prepare(**kwargs) -> None:
    input_path = kwargs["input"]
    output_path = kwargs["output"]
    openai_model = kwargs["model"]
    if not openai_model:
        openai_model = OPENAI_MODEL
    data_parser.prepare_data_to_fine_tune_openai(
        input_path, output_path, openai_model)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", type=str, default="./data/train.jsonl",
                           help="JSONL file containing clickbaits data examples for training.")
    argparser.add_argument("-o", "--output", type=str, default="./data/parsed/train.jsonl",
                           help="JSONL file to be save containing prompt-completion examples for training.")
    argparser.add_argument("-m", "--model", type=str, default="",
                           help="OpenAI model name.")
    args = vars(argparser.parse_args())
    prepare(**args)
