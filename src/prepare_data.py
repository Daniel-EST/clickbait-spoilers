
import logging
import argparse
import os

import data_parser

logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)


def prepare(**kwargs) -> None:
    input_path = kwargs["input"]
    output_path = kwargs["output"]
    if kwargs["test"]:
        test_path = f"{os.path.dirname(output_path)}/test.jsonl"
        val_path = f"{os.path.dirname(output_path)}/validation.jsonl"
        data_parser.prepare_data_test(
            input_path, test_path, val_path, kwargs["test_split"])
    else:
        data_parser.prepare_data_to_fine_tune(input_path, output_path)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", type=str, default="./data/train.jsonl",
                           help="JSONL file containing clickbaits data examples for training.")
    argparser.add_argument("-o", "--output", type=str, default="./data/parsed/train.jsonl",
                           help="JSONL file to be save containing prompt-completion examples for training.")
    argparser.add_argument("--test", type=bool, default=False,
                           help="Splits the JSONL file in train and test")
    argparser.add_argument("--test-split", type=float,
                           default=0.75, help="Proportion of the test split")
    args = vars(argparser.parse_args())
    prepare(**args)
