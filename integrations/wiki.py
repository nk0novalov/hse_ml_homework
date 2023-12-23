import wikipedia
import requests
import json

import api_keys

WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='


def get_wiki_image(search_term, is_actor=True):
    try:
        result = wikipedia.search(search_term, results=1)
        wikipedia.set_lang('en')
        wkpage = wikipedia.WikipediaPage(title=result[0])
        title = wkpage.title
        response = requests.get(WIKI_REQUEST + title)
        json_data = json.loads(response.text)
        img_link = list(json_data['query']['pages'].values())[0]['original']['source']
        return img_link
    except:
        if is_actor:
            return api_keys.DEFAULT_PHOTO_LINK


def get_link_on_page(search_term: str, is_actor=True):
    if not is_actor:
        search_term += " (film)"
    result = wikipedia.search(search_term, results=1)
    wikipedia.set_lang('en')
    wkpage = wikipedia.WikipediaPage(title=result[0])
    return wkpage.url
