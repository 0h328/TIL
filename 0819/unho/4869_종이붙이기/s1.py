'''
DP
1-1, 2-3, 3-5, 4-11, 5-21
찾으려는 인덱스가 홀수이면 이전 인덱스 값*2 - 1
짝수이면 이전 인덱스 값*2 + 1
'''

import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    n = int(input())//10        # n은 10의 배수인데, DP 리스트 인덱스 위해 10을 나누어줌
    dp_list = [0] * (n+1)       # DP list initialize
    dp_list[1] = 1              # 1-1, 2-3, 3-5, 4-11, 5-21
    dp_list[2] = 3

    for idx in range(3, n+1):
        if idx%2:                                       # 홀수이면 이전 인덱스 값*2 - 1
            dp_list[idx] = (dp_list[idx-1] * 2) - 1
        elif not idx%2:                                 # 짝수이면 이전 인덱스 값*2 + 1
            dp_list[idx] = (dp_list[idx-1] * 2) + 1

    answer = dp_list[-1]

    print('#{} {}'.format(tc, answer))