import jsonlines

import datasets


class ClickbaitSpoilersConfig(datasets.BuilderConfig):
    def __init__(self, **kwargs):
        super(ClickbaitSpoilersConfig, self).__init__(**kwargs)


class ClickbaitSpoiler(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        ClickbaitSpoilersConfig(name="clickbait_spoilers",
                                version=datasets.Version("1.0.0")),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "type": datasets.Value("string"),
                    "input": datasets.Value("string"),
                    "instruction": datasets.Value("string"),
                    "output": datasets.Value("string")
                }
            ),
            supervised_keys=None,
        )

    def _split_generators(self, dl_manager):
        downloaded_files = dl_manager.download({
            "train": self.config.data_files["train"],
            "test": self.config.data_files["test"],
            "validation": self.config.data_files["validation"]
        })
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={
                                    "filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={
                                    "filepath": downloaded_files["test"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={
                                    "filepath": downloaded_files["validation"]}),
        ]

    def _generate_examples(self, filepath):
        with jsonlines.open(filepath[0]) as reader:
            for line in reader:
                yield line["id"], line
