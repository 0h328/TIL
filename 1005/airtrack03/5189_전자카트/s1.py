import sys
from itertools import permutations
sys.stdin = open('input.txt')

T = int(input())

def cnt_perm(n, k, total, start):
    global ans
    if k == n-1:
        total += data[start][1]
        if ans > total:
            ans = total
        return

    for i in range(2, n+1):
        if not data[start][i]:
            continue
        if not visited[i]:
            visited[i] = 1
            cnt_perm(n, k+1, total+data[start][i], i)
            visited[i] = 0


for tc in range(1, T+1):
    N = int(input())

    data = [[0] * (N+1)]
    for _ in range(N):
        data.append([0] + list(map(int, input().split())))

    perms = permutations(range(2, N+1))

    visited = [0] * (N+1)

    ans = 100 * N
    # cnt_perm(N, 0, 0, 1)

    for perm in perms:
        start = 1
        temp = 0
        for num in perm:
            temp += data[start][num]
            start = num

        temp += data[perm[-1]][1]

        if temp < ans:
            ans = temp

    print('#{} {}'.format(tc, ans))