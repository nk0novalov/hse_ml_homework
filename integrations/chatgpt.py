import json
from openai import OpenAI
import api_keys

client = OpenAI(
    api_key=api_keys.GPT_KEY,
)

BASE_PROMT_TRANSLATE = "Translate in English in format json with key output this text: "
BASE_PROMT_ACTOR_WHY_1 = "Say in json with key output in 12 words why "
BASE_PROMT_ACTOR_WHY_2 = "is a good actor for film with such twist: "


def base_gpt_request(promt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": promt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    try:
        return json.loads(chat_completion.choices[0].message.content)
    except:
        return {"output": None}


def gpt_translate_text(text_to_translate: str):
    return base_gpt_request(promt=BASE_PROMT_TRANSLATE + text_to_translate)


def why_actor(actor: str, plot: str):
    return base_gpt_request(promt=BASE_PROMT_ACTOR_WHY_1 + actor + BASE_PROMT_ACTOR_WHY_2 + plot)
