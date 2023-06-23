
import logging
import argparse

import data_parser
import random

logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)


def split_data(**kwargs) -> None:
    input_path = kwargs["input"]
    output_folder = kwargs["output"]
    seed = kwargs["seed"]
    if seed:
        random.seed(seed)
    data_parser.prepare_split_data(input_path, output_folder)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", type=str, default="./data/train.jsonl",
                           help="JSONL file containing clickbaits data examples for training.")
    argparser.add_argument("-o", "--output", type=str, default="./data/splitted",
                           help="JSONL file to be save containing prompt-completion examples for training.")
    argparser.add_argument("--split", type=float,
                           default=0.75, help="Proportion of the test split")
    argparser.add_argument("--seed", type=int,
                           default=1337, help="Defines seed")
    args = vars(argparser.parse_args())
    split_data(**args)
