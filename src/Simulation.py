import csv
import datetime
import itertools
import os


from .Deck import DeckFactory
from .Game import Game
from .Battlefield import Battlefield
from .Hand import Hand

class Simulation:
    """
    Simulates games of Magic the Gathering and records the results to a csv file
    """

    def __init__(self, deck_file, num_games=1000, num_turns=10):
        self.num_games = num_games
        self.num_turns = num_turns
        self.deck_factory = DeckFactory(deck_file)
        self.deck = self.deck_factory.create_deck()

        self.deck_file = deck_file
    
    def record_game(self):
        game = Game(battlefield = Battlefield(), deck = self.deck_factory.create_deck(),
                    hand = Hand())
        game.play(self.num_turns)
        return game.history
    
    @staticmethod
    def write_csv(filepath, fieldnames, data):
        with open(filepath, mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = fieldnames, lineterminator = "\n")
            writer.writeheader()
            writer.writerows(itertools.chain(*data))


    @staticmethod
    def generate_save_filepath(deck_file):
        time_format_string = "%Y-%m-%dT%H_%M_%S"
        timestamp = datetime.datetime.now().strftime(time_format_string)
        filepath = f"{deck_file}-{timestamp}.csv"
        return filepath
    
    @staticmethod
    def generate_fieldnames(mana_costs):
        fieldnames = ["game_num", "turn_num"] + [repr(cost) for cost in mana_costs] + ["lands"]
        return fieldnames

    def write_sim_results(self, filepath = None):
        """
        Writes the log of the simulation history as a csv to the input filepath.
        """
        if filepath is None:
            filepath = self.generate_save_filepath(self.deck_file)
        fieldnames = self.generate_fieldnames(self.deck.mana_costs)
        sim_results = self.run_simulation()

        self._write_sim_results(sim_results = sim_results, filepath = filepath, fieldnames = fieldnames)
    
    @staticmethod
    def _write_sim_results(sim_results, filepath, fieldnames = None):
        """
        Writes the log of the simulation history as a csv to the input filepath.
        """

        for game_num, game in enumerate(sim_results, start = 1):
            for turn in game:
                turn.update(game_num = game_num)
                
        if fieldnames is None:
            fieldnames = sim_results[0][0].keys()

        Simulation.write_csv(filepath = filepath, fieldnames = fieldnames, data = sim_results)

    def run_simulation(self):
        return [self.record_game() for _ in range(self.num_games)]



