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
        # print(self.size**2)

    def _add_mines(self):
        mines_cor = self._get_mines_cor()
        for cor in mines_cor:
            self.pool[cor[0]][cor[1]].mine = True

    def _get_mines_cor(self) -> list[tuple[int]]:
        coordinates = set()
        while len(coordinates) < self.mine:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            coordinates.add((x, y))

        return coordinates


g = GamePole(5, 5)
print(g._get_mines_cor())
