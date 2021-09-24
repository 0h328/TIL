import sys
sys.stdin = open('input.txt')


def put_tree(idx, num):
    G[idx] = num

    while idx >= 1 and G[idx//2] > G[idx]:
        G[idx//2], G[idx] = G[idx], G[idx//2]
        idx //= 2


for tc in range(int(input())):
    N = int(input())
    G = [0 for _ in range(N+1)]

    nums = list(map(int, input().split()))

    for idx, num in enumerate(nums):
        put_tree(idx+1, num)

    # print(G)

    ans = 0
    while N > 0:
        ans += G[N//2]
        N //= 2

    print('#{0} {1}'.format(tc+1, ans))
    # break
