import sys

sys.stdin = open('input.txt')

T = int(input())
idx = 1

while idx <= T:
    n = int(input())

    ans_list = [[0] * n for _ in range(n)]
    d = 0           # 방향
    r = c = 0       # 좌표
    input_in_row = n    # 연속으로 입력할 크기 값

    num = 1     # 대입하는 숫자
    while num <= n*n:

        # if nxt_n >= N or nxt_y >= N or ans[nxt_y][nxt_x] != 0

        if d == 0:      # 오른쪽으로 갈 때
            for i in range(input_in_row):   # 3만큼
                ans_list[r][c+i] = num
                num += 1
            else:
                r += 1                      # d == 1에서는 행을 하나씩 증가시키면서 탐색
                c += i                      # 반복문을 돌린 c 값을 저장
                d += 1                      # 방향을 바꿔줌
                input_in_row -= 1           # 열순회 -> 행순회로 바뀌면 입력 크기 값 -1
            continue                        # while 조건을 다시 판단하기 위해 사용. 쓰지 않아도 무방

        if d == 1:      # 아래로 갈 때
            for i in range(input_in_row):
                ans_list[r+i][c] = num      # r를 하나씩 증가시키면서 저장
                num += 1
            else:
                r += i                      # 반복문을 돌린 r 값을 저장
                c -= 1                      # d == 2 에서는 열을 하나씩 줄이면서 탐색
                d += 1                      # 방향 바꿈
            continue

        if d == 2:      # 왼쪽으로 갈 때
            for i in range(input_in_row):
                ans_list[r][c-i] = num      # c를 하나씩 줄이면서 저장
                num += 1
            else:
                r -= 1
                c -= i                      # 반복문을 돌린 c 값을 저장
                d += 1
                input_in_row -= 1           # 열순회 -> 행순회로 바뀌면 입력 크기 값 -1
            continue

        if d == 3:      # 위로 갈 때
            for i in range(input_in_row):
                ans_list[r-i][c] = num      # r를 하나씩 줄이면서 저장
                num += 1
            else:
                r -= i                      # 반복문을 돌린 r 값을 저장
                c += 1
                d -= 3
            continue

    print('#{}'.format(idx))

    for i in range(n):
        for j in range(n):
            print(ans_list[i][j], end=' ')
        print()

    idx += 1
