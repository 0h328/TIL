import sys
sys.stdin = open('input.txt')

#1.
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cost = list(map(int, input().split())) # 가격 입력
#     ans = 0
#
#     for i in range(N-1): # 마지막날은 사도/안사도 그만
#         max_cost = cost[i]
#         for j in range(i+1, N):
#             if max_cost < cost[j]:
#                 max_cost = cost[j]
#
#         if max_cost > cost[i]:
#             ans += max_cost - cost[i] # 이익을 구하자
#     print('#{} {}'.format(tc, ans))

#2.
#########################################################
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cost = list(map(int, input().split())) # 가격 입력
#     ans = 0
#
#     is_sell = [0] * N
#
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if cost[i] < cost[j]:
#                 is_sell[i] = 1
#                 break
#
#     buy_cost = buy_cnt = 0
#
#     for i in range(N):
#         if is_sell[i]:
#             buy_cost += cost[i]
#             buy_cnt += 1
#         else:
#             ans += (cost[i]*buy_cnt) - buy_cost # 이익
#             buy_cost = 0
#             buy_cnt = 0
#     print('#{} {}'.format(tc, ans))


#3.
#########################################################
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split())) # 가격 입력
    ans = 0

    max_cost = cost[-1]

    for i in range(N-2, -1, -1): # 마지막(N-1)은 의미 x
        if max_cost > cost[i]:
            ans += max_cost - cost[i]
        else:
            max_cost = cost[i]

    print('#{} {}'.format(tc, ans))