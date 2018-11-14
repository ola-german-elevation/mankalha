import logging

logger = logging.getLogger("test kalha")
logger.setLevel(logging.DEBUG)


class Player:
    def __init__(self, holes, seeds):
        self.holes = [seeds for x in range(holes)]
        self.home = 0
        self.all_holes_zero = False
        logger.debug(f"Player Init holes: {holes}, seeds: {seeds}")


class KalhaBoard:
    def __init__(self, holes, seeds):
        self.p1 = Player(holes, seeds)
        self.p2 = Player(holes, seeds)
        self.game_over = False
        self.p_turn = 1

    def is_all_holes_zero(self):
        if self.p1.all_holes_zero and self.p2.all_holes_zero:
            self.game_over = True
            return True

        return False

    def check_game_over(self):
        if self.game_over:
            if self.p1.home > self.p2.home:
                return "Player 1 wins"
            elif self.p1.home == self.p2.home:
                return "Tie"
            else:
                return "Player 2 wins"

    def play(self, hole):
        if self.is_all_holes_zero():
            return self.check_game_over()


class Kalha:
    def __init__(self, holes, seeds):
        self.holes = holes
        self.seeds = seeds
        self.board = KalhaBoard(holes, seeds)
        logger.debug(f"Kalha Init: {self}")

    def __str__(self):
        return f'H: {self.holes},S: {self.seeds}'

    def play(self, hole: int) -> object:
        return self.board.play(hole)
