from bs4 import BeautifulSoup
import requests


class MetaDecks:
    def __init__(self):
        self.url = requests.get('https://yugiohtopdecks.com/')
        self.soup = BeautifulSoup(self.url.text, features="html.parser")

    def __get_meta_tags(self):
        for link in self.soup.findAll('td'):
            yield link

    def get_meta_listing(self):
        meta_dict = {}
        tags = self.__get_meta_tags()
        counter = 1
        for items in tags:
            for sub_link in items.findAll('a'):
                for tag in sub_link.findAll('b'):
                    deck = tag.string.replace("\n", '')
                    meta_dict[counter] = deck
                    counter += 1
        return meta_dict

