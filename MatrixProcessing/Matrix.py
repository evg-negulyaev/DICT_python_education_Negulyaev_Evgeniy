class Matrix:
    def __init__(self, size, elements):
        rows = elements.split('\n')
        sizes = size.split(' ')
        x = int(sizes[0])
        y = int(sizes[1])
        self.height = x
        self.width = y
        self.matrix = []
        for i in range(x):
            row = []
            elems = rows[i].split(' ')
            for e in elems:
                row.append(int(e))
            self.matrix.append(row)

    @staticmethod
    def add(matrix1, matrix2):
        matrix1: Matrix
        matrix2: Matrix
        if matrix1.width != matrix2.width or matrix1.height != matrix2.height:
            return None
        rows = []
        for i in range(matrix1.height):
            row = []
            for j in range(matrix1.width):
                row.append(matrix1.matrix[i][j] + matrix2.matrix[i][j])
            rows.append(row)

        res = []
        for row in rows:
            res.append(' '.join(list(map(lambda x: str(x), row))))

        size = str(matrix1.height) + " " + str(matrix1.width)

        return Matrix(size, '\n'.join(res))

    def to_string(self):
        result = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result += str(self.matrix[i][j]) + ' '
            result = result.strip()
            result += '\n'
        return result.strip()
