import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    box = [[0] * 10 for _ in range(10)]

    for i in range(N):
        for j in range(area[i][0], area[i][2] + 1):
            for k in range(area[i][1], area[i][3] + 1):
                box[j][k] += area[i][4]

    cnt = 0
    for s in range(10):
        for t in range(10):
            if box[s][t] >= 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
