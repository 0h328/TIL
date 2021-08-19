def solve(string):
    stack = []
    result = 1
    openers = ['(', '{', '[']
    closers = [')', '}', ']']

    for i in range(len(string)):
        char = string[i]
        if char in openers:
            stack.append(char)
        if char in closers:
            if not len(stack):
                result = 0
                break
            else:
                if char == ')' and stack.pop() != '(':
                    result = 0
                    break
                elif char == '}' and stack.pop() != '{':
                    result = 0
                    break
                elif char == ']' and stack.pop() != '[':
                    result = 0
                    break
    else:
        if len(stack):
            result = 0
    return result

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    code = input()
    ans = solve(code)
    print('#{} {}'.format(tc, ans))