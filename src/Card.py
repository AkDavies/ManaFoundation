#!/usr/bin/python
#-*- coding: utf-8 -*-

class Card:
    def __init__(self, *args, **kwargs):
        self.attributes = dict()
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

