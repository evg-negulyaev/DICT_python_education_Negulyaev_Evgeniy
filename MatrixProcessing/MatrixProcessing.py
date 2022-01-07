from Matrix import Matrix


def enter_matrix(name=''):
    print(f'Enter size of {name}matrix: ', end='')
    size = input()

    height = int(size.split()[0])
    print(f'Enter {name}matrix:')
    res = []
    for _ in range(height):
        res.append(input())
    return Matrix(size, '\n'.join(res))


def main():
    while True:
        print('''1. Add matrices 
2. Multiply matrix by a constant 
3. Multiply matrices 
4. Transpose matrix 
5. Calculate a determinant
6. Inverse matrix
0. Exit ''')
        print('Your choice: ', end='')
        action = input()

        if action == '0':
            break
        elif action == '1':
            matrix1 = enter_matrix('first ')
            matrix2 = enter_matrix('second ')
            result = Matrix.add(matrix1, matrix2)
            if result is None:
                print('ERROR')
            else:
                print('The result is:')
                print(result.to_string())
        elif action == '2':
            matrix = enter_matrix()
            print('Enter constant: ', end='')
            const = float(input())
            result = Matrix.multiply_by_const(matrix, const)
            print('The result is:')
            print(result.to_string())
        elif action == '3':
            matrix1 = enter_matrix('first ')
            matrix2 = enter_matrix('second ')
            result = Matrix.multiply(matrix1, matrix2)
            if result is None:
                print('ERROR')
            else:
                print('The result is:')
                print(result.to_string())
        elif action == '4':
            print('''
1. Main diagonal 
2. Side diagonal 
3. Vertical line 
4. Horizontal line''')
            print('Your choice: ', end='')
            choice = input()

            matrix = enter_matrix()

            result = None
            if choice == '1':
                result = Matrix.transpose_main_diagonal(matrix)
            elif choice == '2':
                result = Matrix.transpose_side_diagonal(matrix)
            elif choice == '3':
                result = Matrix.transpose_vertical(matrix)
            elif choice == '4':
                result = Matrix.transpose_horizontal(matrix)

            if result is None:
                print('ERROR')
            else:
                print('The result is:')
                print(result.to_string())
        elif action == '5':
            matrix = enter_matrix()
            result = matrix.determinant()
            if result is None:
                print('ERROR')
            else:
                print('The result is:')
                print(result)
        elif action == '6':
            matrix = enter_matrix()
            result = Matrix.inverse(matrix)
            if result is None:
                print('ERROR')
            else:
                print('The result is:')
                print(result.to_string())

        print()


if __name__ == '__main__':
    main()
