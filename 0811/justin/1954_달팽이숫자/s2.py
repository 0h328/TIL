def snail(N):
    data = [[0 for _ in range(N)] for _ in range(N)]
    number = 1
    r = c = 0
    move = +1
    for i in range(N, 0, -1):   # 정사각형 크기(N)만큼 반복
        if i == 1:              # 마지막 위치에 왔을 때
            data[c][r] = number
        else:                   # 아니면
            for k in range(i):  # 0 ~ i-1
                data[c][r] = number # 숫자 채우고
                number += 1         # 증가 시키고
                if k == i - 1:      # 마지막 회차
                    c += move       # 가로줄 이동
                else:               # 세로줄 이동
                    r += move
            for k in range(i-1):    # 0 ~ i-2
                data[c][r] = number # 숫자 채우고
                number += 1         # 숫자 증가시키고
                if k == i - 2:      # 마지막 회차
                    move *= -1      # 방향 전환
                    r += move       # 가로줄 이동
                else:               # 세로줄 이동
                    c += move

    return '\n'.join([' '.join(map(str, row)) for row in data])

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = snail(N)
    print('#{}\n{}'.format(tc, ans))