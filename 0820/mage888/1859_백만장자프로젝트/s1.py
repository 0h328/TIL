import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    # print(cost)

    ans = 0

    for i in range(N-1): # 마지막 날은 안사도됨.
        max_cost = cost[i]
        for j in range(i+1, N):
            if max_cost < cost[j]:
                max_cost = cost[j]

        if max_cost > cost[i]:
            ans += max_cost - cost[i]

    print('#{} {}'.format(tc, ans))