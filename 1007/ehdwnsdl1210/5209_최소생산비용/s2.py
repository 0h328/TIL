'''
A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.
각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.
'''

from itertools import permutations

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 987654321

    perm = permutations(range(N), N)
    for i in perm:
        cost = 0
        for j in range(N):
            cost += factory[j][i[j]]
            if cost > min_cost:
                break
        if min_cost > cost:
            min_cost = cost

    print(f'#{tc} {min_cost}')

#1 63
#2 78
#3 129