'''
최대값과 최솟값을 찾아서 값을 구해줌
'''

import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    num = int(input())
    num_list = list(map(int, input().split()))
    max_value = num_list[0]         # 최댓값은 리스트의 제일 첫번째 값으로 할당
    min_value = num_list[0]         # 최솟값은 리스트의 제일 첫번째 값으로 할당

    for n in num_list:              # 숫자가 있는 리스트를 순환
        if max_value < n:           # 최대값보다 큰 값이 있으면 새로 갱신
            max_value = n
        elif min_value > n:         # 최솟값보다 작은 값이 있으면 새로 갱신
            min_value = n

    answer = max_value - min_value

    print('#{} {}'.format(tc, answer))