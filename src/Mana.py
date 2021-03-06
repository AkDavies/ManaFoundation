import re
from collections import Counter
from itertools import groupby
from enum import Enum, unique
from typing import List

@unique
class ManaColors(Enum):
    white = "W"
    blue = "U"
    black = "B"
    red = "R"
    green = "G"
    colorless = "C"

class ManaCombination:
    """
    Represents a combination of different types of mana.
    """

    def __init__(self, mana_counts=None):
        self.mana_symbols = mana_counts if mana_counts  is not None else Counter()
    
    def __getitem__(self, item: str):
        return self.mana_symbols[item]
    
    def __len__(self):
        return sum(self.mana_symbols.values())

    def __repr__(self):
        return repr(self.mana_symbols)
    
    @property
    def cmc(self):
        return len(self)
    
    @classmethod
    def fromSequence(cls, sequence: List[str]):
        return cls(Counter(sequence))
    
class ManaCost:
    """
    Represents the mana payment required to cast a spell or activate an ability.
    """

    def __init__(self):
        self.colored_mana = ManaCombination()
        self.generic_mana = 0
        self.repr_string = None
    
    def __getitem__(self, item: str):
        return self.colored_mana[item]
    
    def __repr__(self):
        return self.repr_string
    
    def is_castable(self, other: ManaCombination):
        colored_mana_requirements = all(self[color] <= other[color] for color in (member.value for member in ManaColors))
        generic_mana_requirement = (len(other) - len(self.colored_mana)) >= self.generic_mana
        return colored_mana_requirements and generic_mana_requirement

    @staticmethod
    def parse_generic_mana(manaCost: str):
        regexp = re.compile(r"{(\d+)}")
        match = regexp.findall(manaCost)
        if match:
            return int(match[0])
        else:
            return 0

    @staticmethod
    def parse_colored_mana(manaCost: str):
        mana_colors = "".join(member.value for member in ManaColors)
        pattern = fr"{{([{mana_colors}])}}"
        regexp = re.compile(pattern)
        return regexp.findall(manaCost)
    
    @classmethod
    def fromString(cls, string: str):
        generic_mana, colored_mana = cls.parse_generic_mana(string), cls.parse_colored_mana(string)

        obj = cls()
        obj.colored_mana = ManaCombination(Counter(colored_mana))
        obj.generic_mana = generic_mana
        obj.repr_string = string.replace("{","").replace("}","")
        
        return obj
    
    @property
    def cmc(self):
        return self.generic_mana + self.colored_mana.cmc