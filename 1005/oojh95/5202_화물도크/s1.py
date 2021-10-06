import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 25
    result = 0
    while N > 0:
        tmp = list(combinations(arr, N))
        for k in range(len(tmp)):
            for i in range(len(tmp[k])):
                for j in range(tmp[k][i][0], tmp[k][i][1]):
                    if not visited[j]:
                        visited[j] = 1
                    else:
                        visited = [0] * 25
                        break
                if not any(visited):
                    break
            else:
                result = N
                break
        N -= 1
        if result > 0:
            break

    print('#{} {}'.format(tc, result))
