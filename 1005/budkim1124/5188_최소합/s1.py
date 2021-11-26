import sys
sys.stdin = open("input.txt")


def solution(x, y):
    global result, total
    dx = [0, 1]
    dy = [1, 0]

    if total > result:
        return

    if x == N - 1 and y == N - 1:
        result = total
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(N) and ny in range(N) and (nx, ny) not in checked:
            checked.append((nx, ny))
            total += arr[nx][ny]
            solution(nx, ny)

            total -= arr[nx][ny]      # dfs 빠져나오면 방문 기록 삭제 & tmp 삭제
            checked.remove((nx, ny))


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    checked = []
    result = 999999999999999
    total = arr[0][0]
    solution(0, 0)
    print("#{} {}".format(t+1, result))

