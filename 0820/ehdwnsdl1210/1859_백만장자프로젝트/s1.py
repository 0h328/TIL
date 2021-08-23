# 마지막날은 무조건 안삼
# 사야하나 팔아야하나 / 나보다 가장 큰값 찾기
# 팔 수 있는지 없는지
# cost += 가격 / cnt += 1
#11312
# 1 사고 1사고 3에 팔고(3 * cnt - cost) cnt 초기화
# 1사고 2팔고 (2 * cnt - cost)

# 반대로 생각?
# 최고값! 역으로 작네? 차이1 / 3이 최고네? 최고 바꿔 / 역으로가면서 차이2 차이2

import sys
sys.stdin = open('input.txt')

'''
# 1) 사야 하나 팔아야 하나

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))  # 가격들 입력

    ans = 0

    # 어디서 많이 본?
    for i in range(N-1): # 어차피 마지막날은 사도 그만 안사도 그만
        max_cost = cost[i]
        for j in range(i+1, N):
            if max_cost < cost[j]:
                max_cost = cost[j]

        if max_cost > cost[i]:
            ans += max_cost - cost[i]   # 이익을 구하기

    print('#{} {}'.format(tc, ans))
'''

'''
# 2) 팔 수 있는지 없는지 체크

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))  # 가격들 입력

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
            ans += (cost[i] * buy_cnt) - buy_cost
            buy_cost = 0
            buy_cnt = 0

    print('#{} {}'.format(tc, ans))
'''


# 3) 반대로 생각해 보자

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))  # 가격들 입력

    ans = 0

    max_cost = cost[-1]

    for i in range(N - 2 , -1, -1):
        # 내가 가진 값보다 보고 있는 값이 작을 때
        if max_cost > cost[i]:
            ans += max_cost - cost[i]
        else:
            max_cost = cost[i]

    print('#{} {}'.format(tc, ans))


