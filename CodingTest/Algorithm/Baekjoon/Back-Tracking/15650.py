# N과 M(2)
import sys
sys.stdin = open('input.txt')

def seq(idx, n, m):
    if idx == m:
        print(*result)
        return
    for j in range(1, n + 1):
        if check[j] == 1:
            continue
        if result[idx-1] < j:
            result[idx] = j
            check[j] = 1
            seq(idx + 1, n, m)
            result[idx] = 0
            check[j] = 0


n, m = map(int, input().split())
check = [0 for _ in range(n+1)]
result = [0 for _ in range(m)]

seq(0, n, m)