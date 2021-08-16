'''
1. 오늘 날짜 가격이 가장 높은 가격이 아니라면 차액을 넣음
2. 하루가 지나면 앞에 있는 요소 삭제
'''


import sys
sys.stdin = open('input.txt')



test_case = int(input())

for tc in range(1, test_case+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.reverse()                            # pop(0) 보다 pop() 이 더 빠름
    answer = 0

    max_price = max(n_list)

    while n_list:
        today = n_list.pop()

        if n_list and today == max_price:       # 오늘 가격이 최고 가격이면, 다음날부터의 최고가격을 다시 찾음
            max_price = max(n_list)             # 다음 최고가 찾아보기만 하고 이익은 없음
            continue

        answer += (max_price - today)           # 이익 계산


    print('#{} {}'.format(tc, answer))