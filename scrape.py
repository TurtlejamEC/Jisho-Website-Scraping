from bs4 import BeautifulSoup
import requests
import urllib.request

with open('words.txt', encoding='utf-8') as f:
    words = [word.strip() for word in f.readlines()]

    for word in words:
        # convert word to %hex format
        converted_word = repr(word.encode('utf-8'))
        converted_word = word[2:-1]
        converted_word = word.replace("\\x", "%")

        # build jisho url
        url = 'https://jisho.org/word/' + converted_word
        req = requests.get(url)
        content = req.text

        # get audio host
        soup = BeautifulSoup(content, features="html.parser")
        audio_src = soup.body.find_all("source")[0]["src"]
        audio_src = "http://" + audio_src[2:]
        
        # download audio
        urllib.request.urlretrieve(audio_src, word + ".mp3")