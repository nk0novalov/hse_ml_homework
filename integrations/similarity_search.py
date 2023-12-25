import os
import sys

from integrations import local_db
from sentence_transformers import SentenceTransformer
from functools import lru_cache
from sklearn.preprocessing import normalize
import faiss
import numpy
import json
import numpy as np


model = SentenceTransformer('stsb-distilbert-base')
index = faiss.IndexFlatIP(768)
precomputed_movie_embs = np.load(str(sys.path[1]) + '/datasets/movie_embeddings.npy')
index.add(precomputed_movie_embs)
f = open(str(sys.path[1]) + '/datasets/embedding_idx_to_movie_id.json')
embedding_idx_to_id = json.load(f)
embedding_idx_to_id = {
    int(key): value for key, value in embedding_idx_to_id.items()
}

def get_recommended_movies(promt, len_output: int):
    search_embedding = model.encode(promt)
    search_embedding = normalize(search_embedding.reshape(1,-1), norm='l2')
    if len_output > 250:
        len_output = 250
    _, I = index.search(search_embedding, len_output)
    movie_ids = [embedding_idx_to_id[idx] for idx in I[0]]
    return movie_ids


