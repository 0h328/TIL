import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    Box = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0     # 하양 : 0, 빨강 : 1, 파랑 : 2, 보라 : 3

    for i in Box:
        if i[-1] == 1:      # 빨강이라면
            for j in range(i[0], i[2] + 1):
                for k in range(i[1], i[3] + 1):
                    if arr[j][k] == 2:      # or arr[j][k] == 3
                        arr[j][k] = 3
                    else:
                        arr[j][k] = 1

        else:       # 파랑이라면
            for l in range(i[0], i[2] + 1):
                for m in range(i[1], i[3] + 1):
                    if arr[l][m] == 1:      # or arr[l][m] == 3
                        arr[l][m] = 3
                    else:
                        arr[l][m] = 2

    for n in arr:       # 보라색은 몇개?
        for o in n:
            if o == 3:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))