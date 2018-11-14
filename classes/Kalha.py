import logging

logger = logging.getLogger("test kalha")
logger.setLevel(logging.DEBUG)


class Player:
    def __init__(self, holes, seeds):
        self.holes = [seeds for x in range(holes)]
        self.sum_Hs = 0
        self.sum_holes_update = True
        self.home = 0
        print(f"Player Init holes: {holes}, seeds: {seeds}")


    def get_sum_holes(self):
        if not self.sum_holes_update:
            self.sum_Hs = sum(self.holes)
        print(self.sum_Hs)
        return self.sum_Hs


class KalhaBoard:
    def __init__(self, holes, seeds):
        self.p1 = Player(holes, seeds)
        self.p2 = Player(holes, seeds)
        self.game_over = False
        self.p_turn = 1

    def is_all_holes_zero(self):
        if self.p1.get_sum_holes() == self.p2.get_sum_holes() == 0:
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
        print(f"Kalha Init: {self}")

    def __str__(self):
        return f'H: {self.holes},S: {self.seeds}'

    def play(self, hole: int) -> object:
        return self.board.play(hole)
