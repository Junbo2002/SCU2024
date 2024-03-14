import requests

from bs4 import BeautifulSoup


def get_img(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser') \
        .find("div", class_="header-new-background-image").get('content')


print(get_img('https://www.last.fm/music/The+Weeknd'))
