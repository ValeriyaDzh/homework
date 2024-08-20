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

    def _add_mines(self):
        mines_cor = self._get_mines_cor(self.mine, self.size - 1)
        print(mines_cor)
        for cor in mines_cor:
            self.pool[cor[0]][cor[1]].mine = True
            self._add_around_mines(cor[0], cor[1])

    def _add_around_mines(self, x: int, y: int):
        for i in range(max(0, x - 1), min(x + 2, self.size)):
            for j in range(max(0, y - 1), min(y + 2, self.size)):
                if i == x and j == y:
                    continue
                else:
                    self.pool[i][j].around_mines += 1

    @staticmethod
    def _get_mines_cor(quantity: int, max_cor: int) -> set[tuple[int]]:
        coordinates = set()
        while len(coordinates) < quantity:
            x = random.randint(0, max_cor)
            y = random.randint(0, max_cor)
            coordinates.add((x, y))

        return coordinates

    def show(self):
        for row in self.pool:
            for cell in row:
                if cell.fl_open:
                    if cell.mine:
                        print("*", end=" ")
                        continue
                    print(cell.around_mines, end=" ")
                else:
                    print("#", end=" ")
            print()
        print("=" * self.size * 2)

    def sellect_cell(self, x: int, y: int):
        if all((isinstance(x, int), isinstance(y, int))):
            cell = self.pool[x][y]
            if cell.mine:
                print("BOOM💥")
            else:
                cell.fl_open = True

        else:
            raise ValueError("The coordinates of the cell must be an integer")

    def open_all_cells(self):
        for row in self.pool:
            for cell in row:
                if not cell.fl_open:
                    cell.fl_open = True


g = GamePole(5, 5)
g.open_all_cells()
g.show()
