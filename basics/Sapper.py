import random


class Cell:

    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open: bool = False

    def __repr__(self):
        return f"{self.mine}"


class GamePole:

    def __init__(self, size: int, mine: int):
        self.size = size
        self.mine = mine
        self.pool = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self._add_mines()
        # for row in self.pool:
        #     print(row)

    def _add_mines(self):
        mines_cor = self._get_mines_cor(self.mine, self.size - 1)
        for cor in mines_cor:
            self.pool[cor[0]][cor[1]].mine = True

    @staticmethod
    def _get_mines_cor(quantity: int, max_cor: int) -> set[tuple[int]]:
        coordinates = set()
        while len(coordinates) < quantity:
            x = random.randint(0, max_cor)
            y = random.randint(0, max_cor)
            coordinates.add((x, y))

        return coordinates


g = GamePole(5, 14)
