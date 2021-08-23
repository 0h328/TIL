'''
동시에 못지나가는 경우
1. 범위 안에 속하는 경우
2. 시작점이나 끝점이 다른 범위안에 들어가는 경우
3. 시작점이나 끝점이 서로 겹치는 경우
'''

import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    n = int(input())
    room_list = [list(map(int, input().split())) for _ in range(n)]
    corridor = [0 for _ in range(401)]

    for s, e in room_list:
        if s > e:               # s 가 더 크면 값 교환
            s, e = e, s
        if not s%2:             # 시작이 짝수이면 1을 뺀다
            s -= 1
        if e%2:                 # 도착이 홀수이면 1을 더한다
            e += 1

        for idx in range(s, e+1):
            corridor[idx] += 1


    answer = max(corridor)
    print('#{} {}'.format(tc, answer))