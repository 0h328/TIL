import sys
from itertools import combinations
sys.stdin = open('input.txt')

def bfs(s, cnt):
    global result
    if s < N-1:
        if not visited[arr[s][0]] and not visited[arr[s][1]-1]:
            cnt += 1
            if cnt > result:
                result = cnt
            for j in range(arr[s][0], arr[s][1]):
                visited[j] = 1
            bfs(s+1, cnt)

        bfs(s+1, cnt)


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 25
    result = 0
    while N > 0:
        tmp = list(combinations(arr, N))

        for i in range(len(tmp[0])):
            for j in range(tmp[0][i][0], tmp[0][i][1]):
                if not visited[j]:
                    visited[j] = 1
                else:
                    visited = [0] * 25
                    N -= 1
                    break
        else:
            result = N
            break
    print('#{} {}'.format(tc, result))