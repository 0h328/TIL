"""
브루트포스 / DFS / 조합 / 백트랙킹 / 최악의 경우 연산 15^10 -> 약 5766억번의 경우의 수 예상
"""

import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')


def solution(swap):
    global answer

    if swap == 0:
        tmp = 0
        for i in range(N):
            tmp += num_li[-1-i] * (10**i)    
        if answer < tmp:
            answer = tmp
        return
    elif visited.get((swap%2, tuple(num_li))):    # backtracking
        return

    visited[(swap%2, tuple(num_li))] = 1
    
    for e in combinations(range(N), 2):
        num_li[e[0]], num_li[e[1]] = num_li[e[1]], num_li[e[0]]
        solution(swap-1)
        num_li[e[0]], num_li[e[1]] = num_li[e[1]], num_li[e[0]]


T = int(input())

for tc in range(1, T+1):
    in_num, swap = map(int, input().split())
    num_li = deque()
    while in_num:                               # 숫자들을 리스트에 넣기
        num_li.appendleft(in_num%10)
        in_num //= 10
    N = len(num_li)

    answer = 0
    visited = {}                                # 방문 체크

    solution(swap)

    print('#{} {}'.format(tc, answer))