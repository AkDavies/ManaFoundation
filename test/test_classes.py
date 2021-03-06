import unittest
from src.Card import Card, CardLibrary
from src.Deck import Deck
from src.Hand import Hand
from src.Battlefield import Battlefield

class TestCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.card_library = CardLibrary()

    def setUp(self):
        self.example_card = self.card_library.get_card(name="Forest")
        self.cryptic_command = self.card_library.get_card(name="Cryptic Command")
    
    def test_constructor(self):
        self.assertEqual(self.cryptic_command.attributes["name"], "Cryptic Command")
        self.assertEqual(self.cryptic_command.attributes["convertedManaCost"], 4.0)
        self.assertEqual(self.cryptic_command.attributes["manaCost"], '{1}{U}{U}{U}')
    
    def test_getitem(self):
        """
        Check whether Card objects support item lookup.
        """
        self.assertEqual(self.cryptic_command["name"], "Cryptic Command")
        self.assertEqual(self.cryptic_command["convertedManaCost"], 4.0)
        self.assertEqual(self.cryptic_command["manaCost"], '{1}{U}{U}{U}')

    def test_tap(self):
        """
        Checks whether tapping a card works.
        """
        self.example_card.untap()
        self.example_card.tap()
        self.assertTrue(self.example_card.is_tapped)
    
    def test_untap(self):
        """
        Checks whether untapping a card works.
        """
        self.example_card.tap()
        self.example_card.untap()
        self.assertFalse(self.example_card.is_tapped)
    
    def test_is_land(self):
        """
        Checks whether or not the is_land property returns True for cards that have the Land card type, and
        False for those that do not.
        """
        self.assertTrue(self.example_card.is_land)
        self.assertTrue(self.card_library.get_card("Island").is_land)

    def test_is_in_play(self):
        pass
    


class TestDeck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.card_library = CardLibrary()

    def setUp(self):
        self.example_card_1 = self.card_library.get_card(name="Plains")
        self.example_card_2 = self.card_library.get_card(name="Island")
        self.example_card_3 = self.card_library.get_card(name="Swamp")
        self.example_card_4 = self.card_library.get_card(name="Mountain")
        self.example_card_5 = self.card_library.get_card(name="Forest")
        self.example_deck = Deck([self.example_card_1,self.example_card_2, self.example_card_3,
                                    self.example_card_4, self.example_card_5
                                ]
                            )
    def test_shuffle(self):
        """
        Checks whether or not the shuffle() method randomly reorders the cards in a Deck.
        """
        self.example_deck.shuffle()
        drawn_card = self.example_deck.draw()
        self.assertIsNot(drawn_card, self.example_card_1)
    
    def test_draw(self):
        """
        Checks whether or not the draw() method correctly removes and returns a Card from a Deck.
        """
        initial_size = self.example_deck.size
        drawn_card = self.example_deck.draw()
        self.assertIsInstance(drawn_card, Card)
        self.assertEqual(self.example_deck.size, initial_size - 1)
    
    def test_add_card(self):
        """
        Checks that the Deck.add_card() method adds a Card to a Deck.
        """
        another_card = self.card_library.get_card(name="Wasteland")
        self.assertNotIn(another_card, self.example_deck)
        self.example_deck._add_card(another_card)
        self.assertIn(another_card, self.example_deck)
    
    def test_add_cards(self):
        """
        Checks that the Deck.add_cards() method adds multiple Cards to a Deck.
        """
        another_card = self.card_library.get_card(name="Wasteland")
        another_card_2 = self.card_library.get_card(name="Strip Mine")
        self.assertNotIn(another_card, self.example_deck)
        self.assertNotIn(another_card_2, self.example_deck)
        self.example_deck._add_cards([another_card,another_card_2])
        self.assertIn(another_card, self.example_deck)
        self.assertIn(another_card_2, self.example_deck)

class TestHand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.card_library = CardLibrary()
    
    def setUp(self):
        self.cards_in_hand = [self.card_library.get_card(name="Island"),self.card_library.get_card(name="Island"),self.card_library.get_card(name="Swamp"), self.card_library.get_card("Cryptic Command")]
        self.example_hand = Hand(cards=self.cards_in_hand)
        self.initial_hand_size = self.example_hand.size
    
    def test_size(self):
        """
        Checks that the Hand.size property returns the number of cards within a Hand.
        """
        self.assertEqual(self.example_hand.size, len(self.cards_in_hand))
    
    def test_draw(self):
        pass
    
    def test_add_card(self):
        """
        Checks that the add_card() method adds a Card to a Hand.
        """
        another_forest = self.card_library.get_card(name="Forest")
        self.assertEqual(self.example_hand.size, self.initial_hand_size)
        self.example_hand.add_card(another_forest)
        self.assertEqual(self.example_hand.size, self.initial_hand_size + 1)
        self.assertIn(another_forest, self.example_hand)
    
    def test_play_land(self):
        """
        Checks that the play_land() method returns a land Card from a deck if one is available.
        """
        output_card = self.example_hand.play_land()
        self.assertIsInstance(output_card, Card)
        self.assertTrue(output_card.is_land)
        self.assertEqual(self.example_hand.size, self.initial_hand_size - 1)

    def test_has_playable_land(self):
        """
        Checks that the has_playable_land property correctly reports whether or not a Hand contains a
        playable land.
        """
        #Example hand starts off with three playable lands, so 
        #after three land plays there should be no more playable lands
        self.assertTrue(self.example_hand.has_playable_land)
        self.example_hand.play_land()
        self.assertTrue(self.example_hand.has_playable_land)
        self.example_hand.play_land()
        self.assertTrue(self.example_hand.has_playable_land)
        self.example_hand.play_land()
        self.assertFalse(self.example_hand.has_playable_land)
    
    def test_land_priority_strategy(self):
        pass

class TestBattlefield(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.card_library = CardLibrary()

    def setUp(self):
        self.island_1 = self.card_library.get_card(name="Island")
        self.battlefield = Battlefield()
    
    def test_play_land(self):
        self.assertNotIn(self.island_1, self.battlefield)
        self.battlefield.play_land(self.island_1)
        self.assertIn(self.island_1, self.battlefield)
    
    def test_untap_lands(self):
        self.island_1.tap()
        self.battlefield.play_land(self.island_1)
        self.assertEqual(self.battlefield.num_tapped_lands, 1)
        self.battlefield.untap_lands()
        self.assertEqual(self.battlefield.num_tapped_lands, 0)
    
    def test_untapped_lands(self):
        untapped_lands = self.battlefield.untapped_lands
        self.assertTrue(all(isinstance(card, Card) and card.is_land and card.is_untapped for card in untapped_lands))
    
    def test_tapped_lands(self):
        self.battlefield.play_land(self.island_1)
        swamp = self.card_library.get_card("Swamp")
        swamp.tap()
        plains = self.card_library.get_card("Plains")
        plains.tap()
        self.battlefield.play_land(swamp)
        self.battlefield.play_land(plains)
        tapped_lands = self.battlefield.tapped_lands
        self.assertTrue(all(isinstance(card, Card) and card.is_land and card.is_tapped for card in tapped_lands))
    
    def test_num_tapped_lands(self):
        swamp = self.card_library.get_card("Swamp")
        swamp.tap()
        plains = self.card_library.get_card("Plains")
        self.assertEqual(self.battlefield.num_untapped_lands, 0)
        self.battlefield.play_land(self.island_1)
        self.assertEqual(self.battlefield.num_tapped_lands, 0)
        self.battlefield.play_land(swamp)
        self.assertEqual(self.battlefield.num_tapped_lands, 1)
        self.battlefield.play_land(plains)
        self.assertEqual(self.battlefield.num_untapped_lands, 2)
    
    def test_num_untapped_lands(self):
        self.assertEqual(self.battlefield.num_untapped_lands, 0)
        self.battlefield.play_land(self.island_1)
        self.assertEqual(self.battlefield.num_untapped_lands, 1)
        self.battlefield.play_land(self.card_library.get_card("Swamp"))
        self.assertEqual(self.battlefield.num_untapped_lands, 2)
        self.battlefield.play_land(self.card_library.get_card("Plains"))
        self.assertEqual(self.battlefield.num_untapped_lands, 3)


class TestGame(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main(verbosity=1)