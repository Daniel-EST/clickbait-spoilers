import logging
import argparse

import data_parser

logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)


def prepare(**kwargs) -> None:
    input_path = kwargs["input"]
    output_path = kwargs["output"]
    data_parser.prepare_data_to_fine_tune_llama(input_path, output_path)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", type=str, default="./data/train.jsonl",
                           help="JSONL file containing clickbaits data examples for training.")
    argparser.add_argument("-o", "--output", type=str, default="./data/parsed/train.jsonl",
                           help="JSONL file to be save containing prompt-completion examples for training.")
    args = vars(argparser.parse_args())
    prepare(**args)
