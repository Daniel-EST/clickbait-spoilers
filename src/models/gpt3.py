import openai
from data_parser import OPENAI_END_OF_COMPLETION, OPENAI_MAX_TOKENS_COMPLETION

TEMPERATURE = 0.07
MAX_TOKENS = OPENAI_MAX_TOKENS_COMPLETION
PRESENCE_PENALTY = 0.0
FREQUENCY_PENALY = 0.0
STOP = [OPENAI_END_OF_COMPLETION]


def predict(clickbait: str, model_id: str) -> str:
    results = openai.Completion.create(
        prompt=clickbait,
        model=model_id,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        presence_penalty=PRESENCE_PENALTY,
        frequency_penalty=FREQUENCY_PENALY,
        stop=STOP
    )
    return [ result.text.strip() for result in results.choices ]
