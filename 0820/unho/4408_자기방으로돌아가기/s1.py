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
