from TicTacToe import TicTacToe


def main():
    print('Enter cells: ', end='')
    cells = input()
    tic_tac_toe = TicTacToe(cells)
    print(tic_tac_toe.to_string())

    while True:
        print('Enter the coordinates:')
        i = j = ''
        try:
            i = int(input())
            j = int(input())
        except ValueError:
            print('You should enter numbers!')
        if i not in range(1, 4) or j not in range(1, 4):
            print('Coordinates should be from 1 to 3!')
        elif tic_tac_toe.cell_is_occupied(i, j):
            print('This cell is occupied! Choose another')
        else:
            tic_tac_toe.add('X', i, j)
            break
    print(tic_tac_toe.to_string())


if __name__ == '__main__':
    main()
