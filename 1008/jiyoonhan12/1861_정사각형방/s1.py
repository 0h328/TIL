import sys
sys.stdin = open('input.txt')

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    can_visit = [0] * (N**2 + 1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + dir[k][0]
                nj = j + dir[k][1]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
                    can_visit[arr[i][j]] = 1

    longest = 1
    cnt = 1
    start = N**2
    for l in range(N**2, -1, -1):
        if can_visit[l]:
            cnt += 1
        else:
            if cnt >= longest:
                longest = cnt
                start = l
            cnt = 1

    print('#{} {} {}'.format(t, start+1, longest))