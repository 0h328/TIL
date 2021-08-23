import sys
sys.stdin = open('input.txt')

T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     cost = list(map(int, input().split()))
#     ans = 0
#
#     for i in range(N-1):    # 마지막 날은 사도 그만 안 사도 그만
#         max_cost = cost[i]  # 왜 인덱스 에러가 나는지...?
#         for j in range(i+1, N):
#             if max_cost < cost[i]:
#                 max_cost = cost[i]
#
#         if max_cost > cost[i]:
#             ans += max_cost - cost[i]   # 이익을 더함
#
#     print('#{} {}'.format(tc, ans))

# 팔 수 있는지 없는지 체크
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    is_sell = [False] * N

    for i in range(N-1):    # 왜 인덱스 에러가 나는지...?
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
            ans += (cost[i] * buy_cnt) - buy_cost

    print('#{} {}'.format(tc, ans))