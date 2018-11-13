import unittest
from classes.Kalha import Kalha

class TestKalha(unittest.TestCase):
    def setUp(self):
        self.game = Kalha(6,6)


    def tearDown(self):
        pass


    def test_good_game(self):
        self.game.play(2)


if __name__ == '__main__':
    unittest.main()


