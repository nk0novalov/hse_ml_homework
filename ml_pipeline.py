from integrations import chatgpt
from integrations.hugingface import query_genre, query_age_rating


def use_pipeline(promt: str):
    eng_txt = chatgpt.gpt_translate_text(promt)
    genres = query_genre(promt)
    age = query_age_rating(promt)

    return {"original": promt,
            "eng_promt": eng_txt,
            "actors": {},
            "sim_films": {},
            "sim_genres": genres,
            "sim_age": age
            }
