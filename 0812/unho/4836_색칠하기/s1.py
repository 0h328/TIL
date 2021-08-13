import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    n = int(input())
    board = [[0]*10 for _ in range(10)]
    answer = 0

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())   # color - 1:빨강 2:파랑 3:보라

        if r1 > r2:
            r1, r2 = r2, r1
        if c1 > c2:
            c1, c2 = c2, c1

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1 and board[i][j] == 0:
                    board[i][j] = 1
                elif color == 1 and board[i][j] == 2:
                    board[i][j] = 3
                elif color == 2 and board[i][j] == 0:
                    board[i][j] = 2
                elif color == 2 and board[i][j] == 1:
                    board[i][j] = 3

    for e in board:
        answer += e.count(3)

    print('#{} {}'.format(tc, answer))