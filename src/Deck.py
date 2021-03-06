#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
import urllib.parse

from .Mana import ManaCost
from .Card import Card

class Deck:
    def __init__(self, cards):
        self.cards = cards

        unique_mana_costs = {card["manaCost"] for card in self if not card.is_land}
        mana_costs = [ManaCost.fromString(mana_cost) for mana_cost in unique_mana_costs]
        mana_costs.sort(key= lambda obj: len(obj.repr_string))
        mana_costs.sort(key= lambda obj: obj.cmc)
        self.mana_costs = mana_costs
    
    def __contains__(self, item):
        return item in self.cards
    
    def __iter__(self):
        yield from self.cards

    #TODO
    def __repr__(self):
        return repr(self.cards)

    @property
    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def _add_card(self, card):
        self.cards.append(card)

    def _add_cards(self, cards):
        self.cards.extend(cards)


class DeckFactory:
    

    def __init__(self, deck_url):
        self.url = deck_url

        parsed_url = urllib.parse.urlparse(deck_url)
        self.scheme = parsed_url.scheme
        if self.scheme == "https" or self.scheme == "http":
            import urllib3
            connection_pool = urllib3.PoolManager()
            response = connection_pool.urlopen("GET", self.url)
            self.deck_data = response.data.decode('utf-8').split("\n")

            # return Deck.from_http(self.url)
        elif self.scheme == '' or self.scheme == "c":
            # return Deck.from_file(self.url)
            with open(self.url) as file:
                self.deck_data = file.readlines()
        else:
            raise Exception("Don't know how to generate a deck from the given URL.")
    
    def create_deck(self):
        deck_list = []
        for line in self.deck_data:
            line = line.strip()
            if line:
                qty, card_name = line.split(maxsplit = 1)
                for _ in range(int(qty)):
                    deck_list.append(Card(card_name))
        deck = Deck(deck_list)
        deck.shuffle()
        return deck
        

