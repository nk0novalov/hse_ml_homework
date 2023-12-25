import sqlite3
import sys

def filter_films(genres, title_ids, is_adult):
    con = sqlite3.connect(str(sys.path[1]) + "/datasets/production_db.db")
    r = con.cursor()

    title_ids_str = '"'+ '","'.join(title_ids) + '"'


    q = f"SELECT id, title, actors, budget, genre_imdb, rating FROM main WHERE id IN ({title_ids_str}) AND (genre_imdb LIKE '%{genres[0]}%')"
    if is_adult:
        q = q + ' AND rating="TV-MA"'

    r.execute(q)
    return r.fetchall()


def get_avg_actors(sql_output: list):
    r = ""
    for x in sql_output:
        r += x[2] + ","
    return r[:-1].split(",")

def get_avg_buget(sql_output: list):
    r = []
    for x in sql_output:
       if x[3]:
         r.append(x[3])
    if r:
        print(r)
        return sum(r)/len(r)
    return None
