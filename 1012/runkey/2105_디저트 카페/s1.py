"""
작은 마름모부터 큰 마름모를 구한 뒤
1부터 N - 2까지 순회
"""

import sys
sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc + 1):
    result = 0

    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            
    print("#{} {}".format(t, result))