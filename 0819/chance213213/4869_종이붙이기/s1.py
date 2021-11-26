#1. 점화식

import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())//10
    paper = [1, 3]

    for i in range(2, N):
        paper.append(2*paper[i-2]+paper[i-1])
    print('#{} {}'.format(tc, paper[-1]))
