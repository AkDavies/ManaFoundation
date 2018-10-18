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

