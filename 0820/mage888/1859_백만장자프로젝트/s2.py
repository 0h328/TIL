import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    is_sell = [False] * N

    for i in range(N-1):
        for j in range(i+1, N):
            if cost[i] < cost[j]:
                is_sell[i] = True
                break

    buy_cost = 0
    buy_cnt = 0

    for i in range(N):
        if is_sell[i]:
            buy_cost += cost[i]
            buy_cnt += 1
        else:
            ans += cost[i] * buy_cnt - buy_cost
            buy_cost = 0
            buy_cnt = 0

    print('#{} {}'.format(tc, ans))
