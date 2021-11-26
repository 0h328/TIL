# 재귀함수 풀이

import sys

sys.stdin = open('input.txt')

T = int(input())

def pascal(num, stack, N):
    if num == N:
        return
    print(' '.join(map(str, stack)))
    new_stack = []
    temp = 0

    while stack:
        pop_num = stack.pop()
        new_stack.append(temp + pop_num)
        temp = pop_num
    new_stack.append(1)

    pascal(num + 1, new_stack, N)

for tc in range(1, T+1):
    N = int(input())
    start_stack = [1]

    print('#{}'.format(tc))
    pascal(0, start_stack, N)