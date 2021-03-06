#!/usr/bin/python
#-*- coding: utf-8 -*-
import json, os

class Card:
    """
    Defines a representation for a Magic: the Gathering card. Contains information about
    various characteristics of the card such as: Name, Mana Cost, Card Type and more.
    """
    def __init__(self, attributes=None, *args, **kwargs):
        self.attributes = attributes
        self.status = {'is_tapped': False}
    
    def __lt__(self, other):
        return self.attributes['name'].__lt__(other.attributes['name'])
    
    def __repr__(self):
        return 'Card({})'.format(self.attributes['name'])
    
    def __getitem__(self, key):
        try:
            return self.attributes[key]
        except:
            raise Exception

    def tap(self, ):
        self.status['is_tapped'] = True

    def untap(self, ):
        self.status['is_tapped'] = False

    @property
    def is_tapped(self, ):
        return self.status['is_tapped']

    @property
    def is_land(self):
        return 'Land' in self.attributes['types']


class CardLibrary:
    library_file_path = "../AllCards.json"
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, library_file_path)

    def __init__(self):
        with open(self.filename, encoding='utf-8') as library_file:
            self.card_library = json.load(library_file)
    
    def get_card(self, name: str) -> Card:
        if name == "Expansion/Explosion":
            name = "Cryptic Command"
        return Card(self.card_library.get(name))