import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split())) # 가격들을 입력

    ans = 0

    #어디서 많이 본 것 같다.
    for i in range(N-1): #어차피 마지막날은 사도 그만 안사도 그만
        max_cost = cost[i]
        for j in range(i+1, N):
            if max_cost < cost[j]:
                max_cost = cost[j]

        if max_cost > cost[i]:
            ans += max_cost - cost[i] #이익을 구하자!!!

    print('#{} {}'.format(test_case, ans))