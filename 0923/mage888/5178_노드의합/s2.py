import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for i in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    for i in range(N, 1, -1):
        tree[i//2] += tree[i]

    print('#{} {}'.format(tc, tree[L]))

