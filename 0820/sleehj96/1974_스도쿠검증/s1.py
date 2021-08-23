import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

i = 1
while i <= T:

    chk = 1

    puzzle = []

    j = 0
    while j < 9:
        puzzle.append(list(map(int, input().split())))
        j += 1

    # print(puzzle)

    # 가로줄 확인
    for e1 in puzzle:
        if set(e1) != set(range(1, 10)):
            chk = 0
            break

    # 세로줄 확인
    tp_puzzle = list(zip(*puzzle))

    for e2 in tp_puzzle:
        if set(e2) != set(range(1, 10)):
            chk = 0
            break

    # 3x3 확인

    for m in range(0, 9, 3):
        for n in range(0, 9, 3):
            divided_puzzle = []
            k = 0
            while k < 3:
                divided_puzzle.append(puzzle[m + k][n:n + 3])
                k += 1

            tmp_set = set()
            for e3 in divided_puzzle:
                tmp_set = tmp_set | set(e3)

            if set(tmp_set) != set(range(1, 10)):
                chk = 0

                break

    print('#{} {}'.format(i, chk))

    i += 1