#!/usr/bin/python
#-*- coding: utf-8 -*-
import csv
from collections import OrderedDict
from itertools import zip_longest

class Game:
    # deck_file = "Deck - Boros Angels.txt"
    # deck_file = "Deck - Golgari Midrange.txt"
    # deck_file = "Deck - Jeskai Control.txt"

    def __init__(self, battlefield, deck, hand):
        self.battlefield = battlefield
        self.hand = hand
        self.deck = deck

        self.land_priority_strategy = lambda card: 1
        self.mulligan_strategy = lambda hand: False
        self.history = None

    def take_turn(self, ):
        pass

    def draw(self, ):
        if self.deck_size > 0:
            drawn_card = self.deck.draw()
            self.hand.add_card(drawn_card)

    def play_land(self, ):
        if self.has_playable_land:
            land = self.hand.play_land()
            self.battlefield.play_land(land)

    @property
    def has_playable_land(self):
        return self.hand.has_playable_land

    @property
    def deck_size(self):
        return self.deck.size 
    
    @property
    def hand_size(self):
        return self.hand.size

    def shuffle_deck(self, ):
        self.deck.shuffle()

    #what to do if n is greater than the number of cards in the deck?
    def draw_n(self, n):
        for _ in range(n):
            self.draw()

    def mulligan(self, n):
        self.return_hand_to_deck()
        self.draw_n(n)

    def return_hand_to_deck(self):
        pass

    def play(self, num_turns):
        #Draw opening hand (players start with seven cards in hand)
        initial_hand_size = 7
        self.draw_n(initial_hand_size)

        #Repeatedly mulligan until we arrive at a "keepable" hand
        #The criteria for keepability are captured by the mulligan strategy
        while self.mulligan_strategy(self.hand):
            self.mulligan(self.hand_size - 1)

        #The following lines play out the specified number of turns and
        #record the available mana combinations on each turn
        fieldnames = ["turn_num"] + [repr(cost) for cost in self.deck.mana_costs] + ["lands"]
        game_result = []
        castable_status = OrderedDict((mana_cost, False) for mana_cost in self.deck.mana_costs)
        uncastable_mana_costs = set(self.deck.mana_costs)
        for turn_num in range(1, 1 + num_turns):
            self.draw()
            if self.has_playable_land:
                self.play_land()
                # Get all of the possible mana combinations that can be produced by the untapped lands currently in play
                mana_combinations = list(self.battlefield.available_mana_combinations)
                # For each of the possible casting costs of spells in the deck determine 
                # whether the cost is payable with the untapped lands currently in play
                for cost in uncastable_mana_costs.copy():
                    if any(cost.is_castable(mana_combo) for mana_combo in mana_combinations):
                        castable_status[cost] = True
                        uncastable_mana_costs.remove(cost)

            castable_results = list(castable_status.values())
            turn_result = [turn_num] + castable_results + [repr(self.battlefield)]
            game_result.append(dict(zip(fieldnames,turn_result)))
        
        self.history = game_result

