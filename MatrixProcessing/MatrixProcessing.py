from Matrix import Matrix


def main():
    size = input()
    height = int(size.split(' ')[0])
    rows = []
    for _ in range(height):
        rows.append(input())
    matrix = Matrix(size, '\n'.join(rows))

    const = int(input())

    result = Matrix.multiply_by_const(matrix, const)
    print(result.to_string())


if __name__ == '__main__':
    main()
