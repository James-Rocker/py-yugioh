import random

from bs4 import BeautifulSoup
import requests


class MetaDecks:
    def __init__(self):
        self.url = 'https://yugiohtopdecks.com/'
        self.meta_dict = {}

    def __get_meta_tags(self):
        request_get = requests.get(self.url)
        soup = BeautifulSoup(request_get.text, features="html.parser")
        for link in soup.findAll('td'):
            yield link

    def get_meta_listing(self):
        tags = self.__get_meta_tags()
        counter = 1
        for items in tags:
            for sub_link in items.findAll('a'):
                for tag in sub_link.findAll('b'):
                    deck = tag.string.replace("\n", '')
                    self.meta_dict[counter] = deck
                    counter += 1
        return self.meta_dict

    def get_all_most_used_cards(self, deck_type=''):
        """
        if no deck_type is passed then a random type will be selected
        :param deck_type:
        :return:
        """
        if deck_type == '':
            deck_type = random.choice(list(self.get_meta_listing().values())).replace(' ', '+')
        most_used_cards_url = f"{self.url}most_used_cards_in_deck/" + deck_type
        get_request = requests.get(most_used_cards_url)
        soup = BeautifulSoup(get_request.text, features="html.parser")
        return soup

    def get_main_deck(self, deck_type=''):
        page = self.get_all_most_used_cards(deck_type)
        return page
