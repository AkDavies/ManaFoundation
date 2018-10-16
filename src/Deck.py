#!/usr/bin/python
#-*- coding: utf-8 -*-
import random

class Deck:
    def __init__(self, cards):
        self.cards = cards
    
    def __contains__(self, item):
        return item in self.cards

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

