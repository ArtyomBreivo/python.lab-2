def create_chessboard(n, m):
    chessboard = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        chessboard.append(row)
    return chessboard

#Пример использования:
n = 5
m = 5
chessboard = create_chessboard(n, m)

for row in chessboard:
    print(" ".join(row))