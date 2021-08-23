'''
스택 - 반복문자지우기와 동일
'''

import sys
sys.stdin = open('input.txt')



for tc in range(1, 11):
    n, in_str = input().split()
    stack = []
    answer = ''

    for c in in_str:
        if not stack or c != stack[-1]:
            stack.append(c)
        elif c == stack[-1]:
            stack.pop()

    for c in stack:
        answer += c

    print('#{} {}'.format(tc, answer))