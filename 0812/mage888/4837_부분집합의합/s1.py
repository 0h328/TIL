import sys
sys.stdin = open('input.txt')

T = int(input())
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(a) # 12

for test_case in range(1, T+1):
    N, K = list(map(int,input().split())) # 3, 6 / 5, 15 / 5, 10

    result = 0                      # N이면서, K인 조건을 출력하기 위해 초기화를 0으로 설정

    for i in range(1 << n):         # 부분집합의 수가 2^n 이므로! # for i in range((1<<N) - 1, 1<<12) 메모리 절약
        a_list = []                 # 각 부분집합을 넣어주기 위해 임의 리스트 설정
        for j in range(n):          # 0~11 # A_list의 index만큼 돌리기 위해서 n으로 설정
            if i & (1 << j):        # i는 2^12 만큼 반복되고, (1 << j)는 n개 만큼 1개씩 i와 비교
                a_list.append(a[j]) # 조건문에 해당되면, A_list에 추가

        if len(a_list) == N and sum(a_list) == K:
            # len(A_list)의 의미 : 부분 집합 중 N개의 원소를 가지고 있는 것 = A_list 내 list의 길이가 N인 것
            # sum(A_list)의 의미 : 부분 집합 중 원소의 합이 K인 것
            result += 1


    print('#{} {}'.format(test_case, result))



