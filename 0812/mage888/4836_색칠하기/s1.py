import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    rc = [[0 for _ in range(10)] for _ in range(10)]
    # print(DataFrame(k))
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                rc[r][c] += color

    result = 0
    for k in range(10):
        for l in range(10):
            if rc[k][l] == 3:
                result += 1

    print('#{} {}'.format(tc, result))


