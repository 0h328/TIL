def is_pair():

    for i in range(len(b)):
        if b[i] == '(' or b[i] == '{':
            s.append(b[i])
        elif b[i] == ')':
            if not s:
                return 0
            elif '{' in s:
                return 0
            elif '{' not in s:
               if '(' in s:
                   s.pop()
        elif b[i] == '}':
            if not s:
                return 0
            elif '{' in s:
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


# tc 8/10