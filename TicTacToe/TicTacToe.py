class TicTacToe:
    def __init__(self, inp='_________'):
        self.field = [[inp[0], inp[1], inp[2]],
                      [inp[3], inp[4], inp[5]],
                      [inp[6], inp[7], inp[8]]]

    def difference(self):
        x = o = 0
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == 'X':
                    x += 1
                elif self.field[i][j] == 'O':
                    o += 1
        return abs(x - o)

    def x_wins(self):
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] == 'X':
                return True
        for j in range(3):
            if self.field[0][j] == self.field[1][j] == self.field[2][j] == 'X':
                return True
        if self.field[0][0] == self.field[0][1] == self.field[0][2] == 'X':
            return True
        if self.field[0][2] == self.field[1][1] == self.field[2][0] == 'X':
            return True
        return False

    def o_wins(self):
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] == 'O':
                return True
        for j in range(3):
            if self.field[0][j] == self.field[1][j] == self.field[2][j] == 'O':
                return True
        if self.field[0][0] == self.field[0][1] == self.field[0][2] == 'O':
            return True
        if self.field[0][2] == self.field[1][1] == self.field[2][0] == 'O':
            return True
        return False

    def is_impossible(self):
        d = self.difference()
        if d not in [0, 1]:
            return True
        return self.x_wins() and self.o_wins()

    def field_is_filled(self):
        for i in range(3):
            for j in range(3):
                if self.field[i][j] not in ['X', 'O']:
                    return False
        return True

    def state(self):
        if self.is_impossible():
            return 'Impossible'
        elif self.x_wins():
            return 'X wins'
        elif self.o_wins():
            return 'O wins'
        elif self.field_is_filled():
            return 'Draw'
        else:
            return 'Game not finished'

    def cell_is_occupied(self, i, j):
        return self.field[i - 1][j - 1] in ['X', 'O']

    def add(self, cell, i, j):
        if not self.cell_is_occupied(i, j):
            self.field[i - 1][j - 1] = cell

    def to_string(self):
        result = '---------\n'
        for i in range(3):
            result += '| '
            for j in range(3):
                result += self.field[i][j] + ' '
            result += '|\n'
        result += '---------'
        return result
