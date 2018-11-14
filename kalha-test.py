import unittest
import logging
from classes.Kalha import Kalha

logger = logging.getLogger("test kalha")
logger.setLevel(logging.DEBUG)


class TestKalha(unittest.TestCase):
    def setUp(self):
        self.game = Kalha(6, 6)
        self.empty_game = Kalha(0, 0)

    def tearDown(self):
        pass

    def test_good_game(self):
        self.game.play(2)
        self.assertEqual(self.empty_game.play(0), "Tie" )


if __name__ == '__main__':
    unittest.main()
