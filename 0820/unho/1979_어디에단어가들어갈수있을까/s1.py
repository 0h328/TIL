'''

'''

import sys
sys.stdin = open('input.txt')



test_case = int(input())

for tc in range(1, test_case+1):
    n, k = map(int, input().split())
    board = [input().replace(' ', '') for _ in range(n)]
    board.extend(map(lambda x: ''.join(x), zip(*board)))        # 가로 세로의 문자열 담은 리스트
    len_list = []                                               # 들어갈수있는 문자열 길이를 담은 리스트

    for e in board:
        len_list.extend(map(lambda x: len(x), e.split('0')))

    answer = len_list.count(k)

    print('#{} {}'.format(tc, answer))