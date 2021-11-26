import sys

sys.stdin = open('input.txt')

T = int(input())

dx = [1, 0]
dy = [0, 1]


def find_min(x, y, cnt):
    global ans
    if x == y == N - 1:
        if cnt < ans:
            ans = cnt
        return
    for i in range(2):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N and visit[new_y][new_x] == 0:
            if mountain[y][x] < mountain[new_y][new_x]:
                cnt += mountain[new_y][new_x] - mountain[y][x]
            visit[new_y][new_x] = 1
            find_min(new_x, new_y, cnt + 1)
            if mountain[y][x] < mountain[new_y][new_x]:
                cnt -= mountain[new_y][new_x] - mountain[y][x]

            visit[new_y][new_x] = 0


for tc in range(1, T + 1):
    N = int(input())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    ans = 987654321
    find_min(0, 0, 0)
    print('#{} {}'.format(tc,ans))
