#!/usr/bin/python
#-*- coding: utf-8 -*-

class Battlefield:
    def __init__(self):
        self.lands = []
    
    def __contains__(self, item):
        return item in self.lands

    def untap_lands(self):
        for land in self.lands:
            if land.is_tapped:
                land.untap()

    #Handle etb triggers/state here?
    def play_land(self, land):
        self.lands.append(land)
    
    @property
    def untapped_lands(self):
        if self.lands:
            return [land for land in self.lands if land.is_untapped]
        return []
    
    @property
    def tapped_lands(self):
        if self.lands:
            return [land for land in self.lands if land.is_tapped]
        return []

    @property
    def num_tapped_lands(self):
        return len(self.tapped_lands)
    
    @property
    def num_untapped_lands(self):
        return len(self.untapped_lands)

