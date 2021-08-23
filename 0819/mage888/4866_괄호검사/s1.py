def is_pair():

    for i in range(len(b)):
        if b[i] == '(' or b[i] == '{':
            s.append(b[i])
        elif b[i] == ')':
            if len(s) == 0:
                return 0
            elif s[-1] is not '(':
                return 0
            elif s[-1] == '(':
                s.pop()
        elif b[i] == '}':
            if len(s) == 0:
                return 0
            elif s[-1] is not '{':
                return 0
            elif s[-1] == '{':
                s.pop()

    if not s:
        return 1

    return 0

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    b = input()
    s = []

    print('#{} {}'.format(tc, is_pair()))


