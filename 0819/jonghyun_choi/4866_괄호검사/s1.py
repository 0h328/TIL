import sys
sys.stdin = open('input.txt')

T = int(input())
open_bracket = '({'
close_bracket = ')}'
for case in range(T):
    data = input()
    stack = []
    for i in data:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            if len(stack) == 0:
                stack.append('error')
                break
            if len(stack) > 0 and stack.pop() != open_bracket[close_bracket.find(i)]:
                break
    if len(stack) == 0:
        print('#{} {}'.format(case + 1, 1))
    else:
        print('#{} {}'.format(case + 1, 0))