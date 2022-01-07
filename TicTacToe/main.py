from TicTacToe import TicTacToe


def main():
    print('Enter cells: ', end='')
    cells = input()
    tic_tac_toe = TicTacToe(cells)
    print(tic_tac_toe.to_string())
    print(tic_tac_toe.state())


if __name__ == '__main__':
    main()
