import unittest
from src.Card import Card
from src.Deck import Deck
from src.Hand import Hand

class TestCard(unittest.TestCase):
    def setUp(self):
        self.example_card = Card(name="Forest")
        self.cryptic_command = Card(name="Cryptic Command")
    
    def test_constructor(self):
        self.assertEqual(self.cryptic_command.attributes["name"], "Cryptic Command")
        self.assertEqual(self.cryptic_command.attributes["convertedManaCost"], 4.0)
        self.assertEqual(self.cryptic_command.attributes["manaCost"], '{1}{U}{U}{U}')

    def test_tap(self):
        self.example_card.untap()
        self.example_card.tap()
        self.assertTrue(self.example_card.is_tapped())
    
    def test_untap(self):
        self.example_card.tap()
        self.example_card.untap()
        self.assertTrue(self.example_card.is_untapped())
    
    def test_is_land(self):
        self.assertTrue(self.example_card.is_land())
        self.assertTrue(Card("Island").is_land())

    def test_is_in_play(self):
        pass
    


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.example_card_1 = Card(name="Plains")
        self.example_card_2 = Card(name="Island")
        self.example_card_3 = Card(name="Swamp")
        self.example_card_4 = Card(name="Mountain")
        self.example_card_5 = Card(name="Forest")
        self.example_deck = Deck([self.example_card_1,self.example_card_2, self.example_card_3,
                                    self.example_card_4, self.example_card_5
                                ]
                            )
    def test_shuffle(self):
        self.example_deck.shuffle()
        drawn_card = self.example_deck.draw()
        self.assertIsNot(drawn_card, self.example_card_1)
    
    def test_draw(self):
        initial_size = self.example_deck.size
        drawn_card = self.example_deck.draw()
        self.assertIsInstance(drawn_card, Card)
        self.assertEqual(self.example_deck.size, initial_size - 1)
    
    def test__add_card(self):
        another_card = Card(name="Wasteland")
        self.assertNotIn(another_card, self.example_deck)
        self.example_deck._add_card(another_card)
        self.assertIn(another_card, self.example_deck)
    
    def test__add_cards(self):
        another_card = Card(name="Wasteland")
        another_card_2 = Card(name="Strip Mine")
        self.assertNotIn(another_card, self.example_deck)
        self.assertNotIn(another_card_2, self.example_deck)
        self.example_deck._add_cards([another_card,another_card_2])
        self.assertIn(another_card, self.example_deck)
        self.assertIn(another_card_2, self.example_deck)

class TestHand(unittest.TestCase):
    
    def setUp(self):
        self.cards_in_hand = [Card(name="Island"),Card(name="Island"),Card(name="Swamp"), Card("Cryptic Command")]
        self.example_hand = Hand(cards=self.cards_in_hand)
        self.initial_hand_size = self.example_hand.size
    
    def test_size(self):
        self.assertEqual(self.example_hand.size, len(self.cards_in_hand))
    
    def test_draw(self):
        pass
    
    def test_add_card(self):
        another_forest = Card(name="Forest")
        self.assertEqual(self.example_hand.size, self.initial_hand_size)
        self.example_hand.add_card(another_forest)
        self.assertEqual(self.example_hand.size, self.initial_hand_size + 1)
        self.assertIn(another_forest, self.example_hand)
    
    def test_play_land(self):
        output_card = self.example_hand.play_land()
        self.assertIsInstance(output_card, Card)
        self.assertTrue(output_card.is_land())
        self.assertEqual(self.example_hand.size, self.initial_hand_size - 1)

    def test_has_playable_land(self):
        #Example hand starts off with three playable lands, so 
        #after three land plays there should be no more playable lands
        self.assertTrue(self.example_hand.has_playable_land())
        self.example_hand.play_land()
        self.assertTrue(self.example_hand.has_playable_land())
        self.example_hand.play_land()
        self.assertTrue(self.example_hand.has_playable_land())
        self.example_hand.play_land()
        self.assertFalse(self.example_hand.has_playable_land())
    
    def test_land_priority_strategy(self):
        pass

class TestBattlefield(unittest.TestCase):
    pass

class TestGame(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main(verbosity=1)