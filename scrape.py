from bs4 import BeautifulSoup
import requests

with open('words.txt', encoding='utf-8') as f:
    words = [word[:-1] for word in f.readlines()]

    for word in words:
        url = 'https://jisho.org/word/' + word
        req = requests.get(url)
        content = req.text

        soup = BeautifulSoup(content)
        print(soup)