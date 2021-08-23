import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    C = input()
    stack = []

    for i in range(len(C)):
        if (C[i] == '{') or (C[i] == '('):
            stack.append(C[i])
        elif C[i] == '}' and len(stack) == 0:
            ans = 0
            break
        elif C[i] == '}' and stack[-1] == '{':
            stack.pop()
        elif C[i] == '}' and stack[-1] == '(':
            ans = 0
            break
        elif C[i] == ')' and len(stack) == 0:
            ans = 0
            break
        elif C[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif C[i] == ')' and stack[-1] == '{':
            ans = 0
            break
    else:
        if len(stack) == 0:
            ans = 1
        else:
            ans = 0

    print('#{} {}'.format(test_case, ans))

