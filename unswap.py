#! /usr/bin/python3

import sys

def testClique(board, clique):
    sum = 0
    for i in clique:
        sum += board[i]
    if sum != 45:
        return False
    return True

def checkCliques(board, cliques):
    errors = []
    for i in range(len(cliques)):
        if not testClique(board, cliques[i]):
            errors.append(i)
    return errors

def testNeighbors(board, n, neighbors):
    for i in neighbors:
        if i == n:
            return False
    return True

def swap(board):
    rcliques = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
                [9, 10, 11, 12, 13, 14, 15, 16, 17],
                [18, 19, 20, 21, 22, 23, 24, 25, 26],
                [27, 28, 29, 30, 31, 32, 33, 34, 35],
                [36, 37, 38, 39, 40, 41, 42, 43, 44],
                [45, 46, 47, 48, 49, 50, 51, 52, 53],
                [54, 55, 56, 57, 58, 59, 60, 61, 62],
                [63, 64, 65, 66, 67, 68, 69, 70, 71],
                [72, 73, 74, 75, 76, 77, 78, 79, 80]
                ]
    ccliques = [[0, 9, 18, 27, 36, 45, 54, 63, 72],
                [1, 10, 19, 28, 37, 46, 55, 64, 73],
                [2, 11, 20, 29, 38, 47, 56, 65, 74],
                [3, 12, 21, 30, 39, 48, 57, 66, 75],
                [4, 13, 22, 31, 40, 49, 58, 67, 76],
                [5, 14, 23, 32, 41, 50, 59, 68, 77],
                [6, 15, 24, 33, 42, 51, 60, 69, 78],
                [7, 16, 25, 34, 43, 52, 61, 70, 79],
                [8, 17, 26, 35, 44, 53, 62, 71, 80]
                ]
    scliques = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
                [3, 4, 5, 12, 13, 14, 21, 22, 23],
                [6, 7, 8, 15, 16, 17, 24, 25, 26],
                [27, 28, 29, 36, 37, 38, 45, 46, 47],
                [30, 31, 32, 39, 40, 41, 48, 49, 50],
                [33, 34, 35, 42, 43, 44, 51, 52, 53],
                [54, 55, 56, 63, 64, 65, 72, 73, 74],
                [57, 58, 59, 66, 67, 68, 75, 76, 77],
                [60, 61, 62, 69, 70, 71, 78, 79, 80]
                ]

    wrongRows = checkCliques(board, rcliques)
    wrongColumns = checkCliques(board, ccliques)
    wrongSquares = checkCliques(board, scliques)

    tiles = []

    if len(wrongRows) == 2 and len(wrongColumns) == 2:
        a = wrongRows[0] * 9 + wrongColumns[0]
        b = wrongRows[0] * 9 + wrongColumns[1]
        c = wrongRows[1] * 9 + wrongColumns[0]
        d = wrongRows[1] * 9 + wrongColumns[1]

        for i in rcliques[wrongRows[0]]:
            if i != a and board[i] == board[a]:
                return (str(a) + "," + str(d) + '\n')
        return (str(b) + "," + str(c) + '\n')

    if len(wrongRows) == 0 and len(wrongSquares) == 2:
        a = (wrongSquares[0]) * 9 + wrongColumns[0]
        b = (wrongSquares[0] + 1) * 9 + wrongColumns[0]
        c = (wrongSquares[0] + 2) * 9 + wrongColumns[0]
        for i in ccliques[wrongColumns[0]]:
            if i != a and board[i] == board[a]:
                return (str(a) + "," + str(a + wrongColumns[1] - wrongColumns[0]) + '\n')
            elif i != b and board[i] == board[b]:
                return (str(b) + "," + str(b + wrongColumns[1] - wrongColumns[0]))
        return (str(c) + "," + str(c + wrongColumns[1] - wrongColumns[0]) + '\n')

    if len(wrongRows) == 0 and len(wrongSquares) == 0:
        tiles = []

        for i in ccliques[wrongColumns[0]]:
            for j in ccliques[wrongColumns[0]]:
                if i != j and board[i] == board[j]:
                    tiles.append(i)
                    tiles.append(j)
                    break
            if len(tiles) == 2:
                break

        for i in ccliques[wrongColumns[1]]:
            for j in ccliques[wrongColumns[1]]:
                if i != j and board[i] == board[j]:
                    tiles.append(i)
                    tiles.append(j)
                    break
            if len(tiles) == 4:
                break

        if tiles[0] // 9 == tiles[2] // 9:
            return (str(tiles[0]) + "," + str(tiles[2]) + '\n')
        return (str(tiles[1]) + "," + str(tiles[3]) + '\n')

    if len(wrongColumns) == 0 and len(wrongSquares) == 2:
        a = wrongRows[0] * 9 + (wrongSquares[0] * 3 % 9)
        b = wrongRows[0] * 9 + (wrongSquares[0] * 3 % 9 + 1)
        c = wrongRows[0] * 9 + (wrongSquares[0] * 3 % 9 + 2)

        for i in rcliques[wrongRows[0]]:
            if i != a and board[i] == board[a]:
                return (str(a) + "," + str(a + wrongRows[1] * 9 - wrongRows[0] * 9) + "\n")
            elif i != b and board[i] == board[b]:
                return (str(b) + "," + str(b + wrongRows[1] * 9 - wrongRows[0] * 9) + "\n")
            elif i != c and board[i] == board[c]:
                return (str(c) + "," + str(c + wrongRows[1] * 9 - wrongRows[0] * 9) + "\n")

    if len(wrongColumns) == 0 and len(wrongSquares) == 0:
        tiles = []

        for i in rcliques[wrongRows[0]]:
            for j in rcliques[wrongRows[0]]:
                if i != j and board[i] == board[j]:
                    tiles.append(i)
                    tiles.append(j)
                    break
            if len(tiles) == 2:
                break

        for i in rcliques[wrongRows[1]]:
            for j in rcliques[wrongRows[1]]:
                if i != j and board[i] == board[j]:
                    tiles.append(i)
                    tiles.append(j)
                    break
            if len(tiles) == 4:
                break
        if tiles[0] // 9 != tiles[2] // 9:
            return (str(tiles[0]) + "," + str(tiles[2]) + '\n')
        return (str(tiles[1]) + "," + str(tiles[3]) + '\n')

def main():
    b = open(sys.argv[1], 'r').read().replace('\n', ',').split("incorrect")
    board = []
    for i in b:
        temp = []
        for j in i.split(','):
            if j.isdigit():
                temp.append(int(j))
        if len(temp) != 0:
            board.append(temp)

    fout = open(sys.argv[2], 'w')

    final = ''
    for i in board:
        final += swap(i)
    fout.write(final)
    fout.close()
main()
