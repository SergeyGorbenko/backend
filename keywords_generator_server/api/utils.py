import re

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def check_url(url):
    www = UserAgent()
    return requests.get(url, headers={'User-Agent': str(www.random)})


def get_title(html):
    soup = BeautifulSoup(html.content, features="html.parser")
    return soup.title.string


def generate_keywords_list(title):
    title_without_special_symbols = re.sub('[\W]+', ' ', str(title))
    title_keywords_list = title_without_special_symbols.split()
    acc = []
    count = 1
    while count <= len(title_keywords_list):
        for i in range(len(title_keywords_list)):
            if i + count <= len(title_keywords_list):
                acc.append(str(" ").join(title_keywords_list[x] for x in range(i, i + count)))
        count += 1
    return acc
