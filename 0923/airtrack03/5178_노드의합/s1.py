import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [0 for _ in range(N+1)]

    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    for i in range(N, L+1, -1):
        tree[i//2] += tree[i]

    ans = tree[L]
    print('#{} {}'.format(tc, ans))