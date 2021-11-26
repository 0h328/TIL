import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            acc = 0
            for k in range(i, i+m):
                for l in range(j, j+m):
                    acc += area[k][l]
            result = max(result, acc)
    print('#{} {}'.format(idx, result))
