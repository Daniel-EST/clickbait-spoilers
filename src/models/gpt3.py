import openai


MODEL_ID = "ada:ft-personal-2023-05-04-01-44-28"


def predict(clickbait: str) -> str:
    results = openai.Completion.create(
        prompt=clickbait,
        model=MODEL_ID,
        temperature=0.07,
        max_tokens=128,
        presence_penalty=0.0,
        frequency_penalty=0.0,
        stop=[" END"]
    )

    return [ result.text.strip() for result in results.choices ]
