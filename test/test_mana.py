import unittest

from src.Mana import ManaCombination, ManaCost
from src.Card import Card, CardLibrary

class TestMana(unittest.TestCase):
    
    def setUp(self):
        self.card_library = CardLibrary()
        self.cryptic_command = self.card_library.get_card(name = "Cryptic Command")
        self.dreadbore = self.card_library.get_card(name = "Dreadbore")
        self.perilous_vault = self.card_library.get_card(name = "Perilous Vault")
        self.steel_leaf_champion = self.card_library.get_card(name = "Steel Leaf Champion")
    
    def test_castablity(self):
        """
        Checks whether or not cards can be cast with lands available.
        """
        cryptic_mana_cost = ManaCost.fromString(self.cryptic_command['manaCost'])
        dreadbore_mana_cost = ManaCost.fromString(self.dreadbore['manaCost'])
        perilous_vault_mana_cost = ManaCost.fromString(self.perilous_vault['manaCost'])
        steel_leaf_champion_mana_cost = ManaCost.fromString(self.steel_leaf_champion['manaCost'])

        mana_combo_1 = ManaCombination.fromSequence(['U','U', "U", "U"])
        mana_combo_2 = ManaCombination.fromSequence(['U','U', "U", "R"])
        mana_combo_3 = ManaCombination.fromSequence(['U','U', "U"])
        self.assertTrue(cryptic_mana_cost.is_castable(mana_combo_1))
        self.assertTrue(cryptic_mana_cost.is_castable(mana_combo_2))
        self.assertFalse(cryptic_mana_cost.is_castable(mana_combo_3))

        mana_combo_4 = ManaCombination.fromSequence(['U','U', "U", "R", "B"])
        self.assertTrue(cryptic_mana_cost.is_castable(mana_combo_4))

        self.assertTrue(dreadbore_mana_cost.is_castable(mana_combo_4))
        self.assertFalse(dreadbore_mana_cost.is_castable(mana_combo_1))
        self.assertFalse(dreadbore_mana_cost.is_castable(mana_combo_2))
        self.assertFalse(dreadbore_mana_cost.is_castable(mana_combo_3))

        self.assertTrue(perilous_vault_mana_cost.is_castable(mana_combo_4))
        self.assertTrue(perilous_vault_mana_cost.is_castable(mana_combo_1))
        self.assertTrue(perilous_vault_mana_cost.is_castable(mana_combo_2))
        self.assertFalse(perilous_vault_mana_cost.is_castable(mana_combo_3))

        self.assertFalse(steel_leaf_champion_mana_cost.is_castable(mana_combo_1))
        self.assertFalse(steel_leaf_champion_mana_cost.is_castable(mana_combo_2))
        self.assertFalse(steel_leaf_champion_mana_cost.is_castable(mana_combo_3))
        self.assertFalse(steel_leaf_champion_mana_cost.is_castable(mana_combo_4))
if __name__ == '__main__':
    unittest.main(verbosity = 1)