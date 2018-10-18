#!/usr/bin/python
#-*- coding: utf-8 -*-
import queue 
class Hand:


    def __init__(self, cards=None):
        self.cards = []
        self.playable_land_queue = queue.PriorityQueue()
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
            item = (self.land_priority_strategy(card),card)
            self.playable_land_queue.put(item)

    def play_land(self, ):
        if self.has_playable_land:
            _, land = self.playable_land_queue.get()
            self.cards.remove(land)
            return land

    @staticmethod
    def land_priority_strategy(card):
        return 1
    
    @property
    def has_playable_land(self, ):
        return not self.playable_land_queue.empty()



