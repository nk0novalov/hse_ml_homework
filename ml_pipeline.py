from integrations import chatgpt
from integrations.hugingface import query_genre, query_age_rating
from integrations.local_db import filter_films, get_avg_actors
from integrations.similarity_search import get_recommended_movies
from integrations import local_db
from integrations import wiki


def exe_pipeline(promt: str):
    eng_txt = chatgpt.gpt_translate_text(promt).get("output", None)
    genres = query_genre(promt)
    top_3_genres = sorted(genres, key=genres.get, reverse=True)
    age = query_age_rating(promt)
    top_age = sorted(age, key=age.get, reverse=True)[:1]
    is_adult = sorted(age, key=age.get, reverse=True)[:1] == ["Adult"]
    titles = get_recommended_movies(promt, 34)
    titles = [t.replace("/title/", "").replace("/", "") for t in titles]
    film_sql_data = (filter_films(top_3_genres[:1], titles, is_adult))

    actors_data = []
    for a in get_avg_actors(film_sql_data)[:4]:
        actors_data.append([a, chatgpt.why_actor(a, promt)['output'], wiki.get_wiki_image(search_term=a,is_actor=True)])
    print(actors_data)
    return {"original": promt,
            "eng_promt": eng_txt,
            "actors": actors_data,
            "sim_films": [x[1] for x in film_sql_data][:3],
            "sim_genres": genres,
            "sim_age": age,
            "sim_titles": titles,
            "is_adult": is_adult,
            "top_genre": top_3_genres[:3],
            "top_age": top_age
            }

