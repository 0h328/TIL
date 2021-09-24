import sys
sys.stdin = open('input.txt')


def pre_order(t):
    global cnt
    if t:
        cnt += 1
        pre_order(tree[t][0])
        pre_order(tree[t][1])

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split()) # E: 간선, N : 서브트리 루트
    tree = [[0, 0] for _ in range(E + 2)]
    nums = list(map(int, input().split()))
    cnt = 0

    for i in range(E):
        if not tree[nums[2 * i]][0]:
            tree[nums[2 * i]][0] = nums[2 * i + 1]
        else:
            tree[nums[2 * i]][1] = nums[2 * i + 1]
    pre_order(N)

    print('#{} {}'.format(t, cnt))