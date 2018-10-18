#!/usr/bin/python
#-*- coding: utf-8 -*-
import json, os

class Card:
    library_file_path = "../AllCards.json"
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, library_file_path)
    library_file = open(filename, encoding='utf-8')
    card_library = json.load(library_file)

    def __init__(self, name, *args, **kwargs):
        self.attributes = Card.card_library.get(name)
        self.status = {'is_tapped': False}
    
    # def __eq__(self, other):
    #     return self.attributes['name'].__eq__(other.attributes['name'])
    
    def __lt__(self, other):
        return self.attributes['name'].__lt__(other.attributes['name'])
    
    def __repr__(self):
        return 'Card({})'.format(self.attributes['name'])

    def tap(self, ):
        self.status['is_tapped'] = True

    def untap(self, ):
        self.status['is_tapped'] = False

    def is_in_play(self, ):
        pass

    def is_tapped(self, ):
        return self.status['is_tapped'] == True

    def is_untapped(self, ):
        return not self.is_tapped()
    
    def is_land(self):
        return 'Land' in self.attributes['types']

