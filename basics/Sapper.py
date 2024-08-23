import random


class Cell:

    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open: bool = False

    def __repr__(self):
        if self.mine:
            return f"{"*" if self.fl_open else "#"}"
        return f"{self.around_mines if self.fl_open else "#"}"


class GamePole:

    def __init__(self, size: int, mine: int):
        self.size = size
        self.mine = mine
        self.pool = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.save_cell = size**2 - mine
        self._add_mines()

    def _add_mines(self):
        mines_cor = self._get_mines_cor(self.mine, self.size - 1)
        for x, y in mines_cor:
            self.pool[x][y].mine = True
            self._add_around_mines(x, y)

    def _add_around_mines(self, x: int, y: int):
        cors = self.get_neighbors(x, y, self.size)
        for x, y in cors:
            self.pool[x][y].around_mines += 1

    @staticmethod
    def _get_mines_cor(quantity: int, max_cor: int) -> set[tuple[int]]:
        coordinates = set()
        while len(coordinates) < quantity:
            x = random.randint(0, max_cor)
            y = random.randint(0, max_cor)
            coordinates.add((x, y))

        return coordinates

    def show(self, all=False):
        if all:
            self._open_all_cells()
        for row in self.pool:
            print(" ".join(str(cell) for cell in row))
        print("=" * self.size * 2)

    def sellect_cell(self, x: int, y: int):
        if all((isinstance(x, int), isinstance(y, int))):
            cell = self.pool[x][y]
            if cell.fl_open:
                return
            if cell.mine:
                return True

            cell.fl_open = True
            self.save_cell -= 1
            if cell.around_mines == 0:
                for i in range(max(0, x - 1), min(x + 2, self.size)):
                    for j in range(max(0, y - 1), min(y + 2, self.size)):
                        if i == x and j == y:
                            continue
                        self.sellect_cell(i, j)

            return
        else:
            raise ValueError
        
    @staticmethod
    def get_neighbors(x: int, y: int, max_int: int) -> list[tuple[int]]:
        neighbors_cor = []
        for i in range(max(0, x - 1), min(x + 2, max_int)):
            for j in range(max(0, y - 1), min(y + 2, max_int)):
                if i == x and j == y:
                    continue
            neighbors_cor.append((i, j))

        return neighbors_cor

    def _open_all_cells(self):
        for row in self.pool:
            for cell in row:
                if not cell.fl_open:
                    cell.fl_open = True

    def start(self):

        while True:
            try:
                self.show()
                ux, uy = map(int, input("\nEnter the coordinates of the cell separated by a space(row column): \n").split())
                if 1 <= ux < self.size + 1 and 1 <= uy < self.size + 1:
                    if self.sellect_cell(ux - 1, uy - 1):
                        print("\nBOOM💥\nGame over\n")
                        self.show(all=True)
                        break
                    else:
                        if self.save_cell == 0:
                            print("\nVictory🎉\n")
                            self.show(all=True)
                            print("\nThank you for playing!\nSee you next time!")
                            break
                else:
                    raise ValueError
            except ValueError:
                print("\n!!The coordinates of the cell must be a positive number, no more than the size of the field!!\n")


pole_game = GamePole(10, 12)
pole_game.start()
