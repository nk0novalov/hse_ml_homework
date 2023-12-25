from integrations import chatgpt
from integrations.hugingface import query_genre, query_age_rating
from integrations.local_db import filter_films, get_avg_actors
from integrations.similarity_search import get_recommended_movies
from integrations import local_db


def exe_pipeline(promt: str):
    eng_txt = chatgpt.gpt_translate_text(promt).get("output", None)
    genres = query_genre(promt)
    top_3_genres = sorted(genres, key=genres.get, reverse=True)[:1]
    age = query_age_rating(promt)
    is_adult = sorted(age, key=age.get, reverse=True)[:1] == ["Adult"]
    titles = get_recommended_movies(promt, 34)
    titles = [t.replace("/title/", "").replace("/", "") for t in titles]
    film_sql_data = (filter_films(top_3_genres, titles, is_adult))
    print(film_sql_data)


    print(filter_films(title_ids=titles, genres=top_3_genres, is_adult=False))
    return {"original": promt,
            "eng_promt": eng_txt,
            "actors": get_avg_actors(film_sql_data),
            "sim_films": [x[1] for x in film_sql_data][:3],
            "sim_genres": genres,
            "sim_age": age,
            "sim_titles": titles,
            "is_adult": is_adult,
            "top_genre": top_3_genres
            }

