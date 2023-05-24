import jsonlines

import datasets
from datasets.tasks import QuestionAnsweringExtractive


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
                    "context": datasets.Value("string"),
                    "question": datasets.Value("string"),
                    "answers": datasets.features.Sequence(
                        {
                            "text": datasets.Value("string"),
                            "answer_start": datasets.Value("int32"),
                        }
                    ),
                }
            ),
            supervised_keys=None,
            task_templates=[
                QuestionAnsweringExtractive(
                    question_column="question", context_column="context", answers_column="answers"
                )
            ],
        )

    def _split_generators(self, dl_manager):  # datasets.DownloadManager._download
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
        with jsonlines.open(filepath[0]) as f:
            for example in f:
                yield example["id"], example
