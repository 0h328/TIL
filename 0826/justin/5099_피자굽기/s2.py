def solve(N, M, arr):
    Q = []
    for i in range(1, N+1):
        Q.append(i)
    idx = N + 1
    top = 0
    while Q:
        top = Q.pop(0)
        if arr[top] // 2 != 0:
            arr[top] //= 2
            Q.append(top)
        elif idx <= M:
            Q.append(idx)
            idx += 1
    return top


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    ans = solve(N, M, arr)
    print('#{} {}'.format(tc, ans))