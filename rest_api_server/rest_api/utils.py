import requests


def get_keywords_from_keywords_generation_server(url):
    r = requests.post('http://127.0.0.1:9999/keywords_generator/api/keywords/',
                      data={'url': url})
    return r.json()['keywords']

