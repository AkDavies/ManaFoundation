import unittest
from src.Card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.example_card = Card(name="Forest")

    def test_tap(self):
        self.example_card.untap()
        self.example_card.tap()
        self.assertTrue(self.example_card.is_tapped())
    
    def test_untap(self):
        self.example_card.tap()
        self.example_card.untap()
        self.assertTrue(self.example_card.is_untapped())
    
    def test_is_in_play(self):
        pass
    


class TestDeck(unittest.TestCase):
    def test_shuffle(self):
        pass
    
    def test_draw(self):
        pass

class TestHand(unittest.TestCase):
    pass

class TestBattlefield(unittest.TestCase):
    pass

class TestGame(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()