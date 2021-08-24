import sys

sys.stdin = open('input.txt')

T = int(input())
idx = 1

while idx <= T:
    n = int(input())

    ans_list = [[0] * n for _ in range(n)]
    d = 0       # 방향
    r = c = 0   # 최초 좌표
    input_in_row = n    # 연속으로 입력할 크기 값

    num = 1     # 대입할 숫자
    while num <= n*n:
        if d == 0:      # 오른쪽으로 갈 때
            for i in range(input_in_row):
                ans_list[r][c+i] = num      # 열을 하나씩 증가시키면서 저장
                num += 1
            else:
                r += 1      # 다음 대입할 r 갱신
                c += i      # 위에서 반복한 c로 갱신

        if d == 1:      # 아래로 갈 때
            for i in range(input_in_row):
                ans_list[r+i][c] = num
                num += 1
            else:
                r += i
                c -= 1

        if d == 2:      # 왼쪽으로 갈 때
            for i in range(input_in_row):
                ans_list[r][c-i] = num
                num += 1
            else:
                r -= 1
                c -= i

        if d == 3:      # 위로갈 때
            for i in range(input_in_row):
                ans_list[r-i][c] = num
                num += 1
            else:
                r -= i
                c += 1

        if not d & 1:           # 짝수면 == 열 순회에서 행 순회로 바뀌면
            input_in_row -= 1   # 입력 범위를 하나 줄임

        d = (d + 1) % 4         # 방향 바꿈

    print('#{}'.format(idx))

    for i in range(n):
        for j in range(n):
            print(ans_list[i][j], end=' ')
        print()

    idx += 1
