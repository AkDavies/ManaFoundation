#!/usr/bin/python
#-*- coding: utf-8 -*-
import itertools

from .Mana import ManaCombination


class Battlefield:
    def __init__(self):
        self.lands = []
    
    def __contains__(self, item):
        return item in self.lands
    
    def __repr__(self):
        return self.lands.__repr__()

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
            return [land for land in self.lands if not land.is_tapped]
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

    @property
    def available_mana_combinations(self):
        mana = [land.attributes["colorIdentity"] if land.attributes["colorIdentity"] else "C" for land in self.lands]
        available_combos = set()
        for num_lands in range(1, len(mana) + 1):
            for land_combo in itertools.combinations(mana, num_lands):
                available_combos |= set(itertools.product(*land_combo))
        return (ManaCombination.fromSequence(combo) for combo in available_combos)