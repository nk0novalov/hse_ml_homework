import requests
import api_keys
API_URL_GENRE = "https://api-inference.huggingface.co/models/nkonovalov/film-genre-detection-0"
API_URL_AGE_RATING = "https://api-inference.huggingface.co/models/austinphamm/netflix_rating_classifier"
headers = {"Authorization": f"Bearer {api_keys.HF_API_KEY}"}


def query_rating_prediction_from_hf(promt: str, api_endpoint: str):
    result = {}
    response = requests.post(api_endpoint, headers=headers, json={"text": promt})
    for item in response.json():
        result[item['label']] = item['score']
    return result


def query_genre(promt: str):
    print(query_rating_prediction_from_hf(api_endpoint=API_URL_GENRE, promt=promt))


def query_age_rating(promt: str):
    print(query_rating_prediction_from_hf(api_endpoint=API_URL_AGE_RATING, promt=promt))

