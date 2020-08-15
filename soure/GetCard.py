import requests


class ScrapeCards:
    """
    Declare the class and then apply the method you want along with the arguments
    """
    def __init__(self):
        self.base_url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'

    def get_single_card(self, card_name=''):
        return requests.get(self.base_url, params={'name': card_name}).json()['data']

    def get_by_attack(self, attack):
        return requests.get(self.base_url, params={'atk': attack}).json()['data']

    def get_by_defence(self, defence):
        return requests.get(self.base_url, params={'def': defence}).json()['data']

    def get_by_level(self, level):
        return requests.get(self.base_url, params={'level': level}).json()['data']

    def get_by_attribute(self, attribute):
        return requests.get(self.base_url, params={'attribute': attribute}).json()['data']

    def get_by_archetype(self, archetype):
        return requests.get(self.base_url, params={'archetype': archetype}).json()['data']

    def get_by_link(self, link):
        return requests.get(self.base_url, params={'link': link}).json()['data']


class GetScrapeValues(ScrapeCards):
    """
    If you don't know what you are looking for then use this class with the get_all_cards_by_args method
    """
    def __init__(self):
        ScrapeCards.__init__(self)
        self.data = requests.get(self.base_url).json()['data']

    def get_all_card_by_args(self, searcher):
        """
        'name', 'fname', 'desc', 'effect', 'sort', 'sortorder', 'num', 'offset', 'type', 'atk', 'def', 'level', 'race',
        'attribute', 'set', 'rarity', 'archetype', 'set', 'banlist', 'link', 'scale', 'linkmarker', 'format', 'staple',
        'misc', 'includeAliased', 'startdate', 'enddate', 'dateregion', 'startprice', 'endprice', 'num', 'offset'
        :param searcher:
        :return:
        """
        unit_list = []
        for card in self.data:
            if searcher in card:
                unit_list.append(card.get(searcher))
        return list(set(unit_list))



# {'error': "No valid parameter set. This API accepts the following parameters: ."}

# print(ScrapeCards().get_single_card('Dark Magician'))
# print(ScrapeCards().get_by_defence(2500))
print(GetScrapeValues().get_all_card_by_args('race'))