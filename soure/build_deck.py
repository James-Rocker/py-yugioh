import random
from get_card import GetScrapeValues, ScrapeCards
# TODO: get an archetype, search it then build a deck list
# TODO: how do we determine what archetype specific cards we should add to a deck?
# TODO: We need a Staples function. What makes a card a staple?
# TODO: We could look into taking a deck type argument to get an archetype


class BuildDeck:
    def __init__(self, archetype=''):
        if archetype == '':
            self.archetype = random.choice(GetScrapeValues().get_all_card_by_args('archetype'))
        else:
            self.archetype = archetype
        self.deck_size = 40
        self.maximum_copies = 3
        self.extra_deck = 15
        self.side_deck = 15
        self.deck_types = [{'Type': 'Aggro'},
                           {'Type': 'Control'},
                           {'Type': 'Combo'},
                           {'Type': 'Ramp'},
                           {'Type': 'Midrange'},
                           {'Type': 'Hybrid'}]

    def return_archetype(self):
        return ScrapeCards().get_by_archetype(self.archetype)

    def get_archetype_cards(self):
        try:
            return ScrapeCards().get_by_archetype(self.archetype)
        except KeyError:
            return 'not a valid archetype'
            pass
