#!/usr/bin/python
#-*- coding: utf-8 -*-
from .MutableHeap import MutableHeap
class Hand:


    def __init__(self, cards=None):
        self.cards = []
        self.playable_land_queue = MutableHeap()
        if cards:
            for card in cards:
                self.add_card(card)

    def __contains__(self, item):
        return item in self.cards

    def __repr__(self):
        return self.cards.__repr__()

    @property
    def size(self):
        return len(self.cards)

    def draw(self, card):
        pass
    
    def add_card(self, card):
        self.cards.append(card)
        if card.is_land:
            self.playable_land_queue.insert(data = card, key = self.land_priority_strategy(card))

    def play_land(self, ):
        if self.has_playable_land:
            land = self.playable_land_queue.pop()
            self.cards.remove(land)
            return land

    @staticmethod
    def land_priority_strategy(card):
        return 1
    
    @property
    def has_playable_land(self, ):
        return bool(self.playable_land_queue)



