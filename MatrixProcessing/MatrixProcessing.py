from Matrix import Matrix


def main():
    size = input()
    height = int(size.split(' ')[0])
    rows1 = []
    for _ in range(height):
        rows1.append(input())
    matrix1 = Matrix(size, '\n'.join(rows1))

    size = input()
    height = int(size.split(' ')[0])
    rows2 = []
    for _ in range(height):
        rows2.append(input())
    matrix2 = Matrix(size, '\n'.join(rows2))

    result = Matrix.add(matrix1, matrix2)
    if result is None:
        print('ERROR')
    else:
        print(result.to_string())


if __name__ == '__main__':
    main()
