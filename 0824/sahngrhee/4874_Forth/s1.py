import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    cal = list(input().split())
    stack = []

    ans = 0
    for i in range(len(cal)):
        if cal[i] == '+':
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(x + y)
            else:
                ans = 'error'
                stack.pop()
        elif cal[i] == '-':
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            else:
                ans = 'error'
                stack.pop()
        elif cal[i] == '*':
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(x * y)
            else:
                ans = 'error'
                stack.pop()
        elif cal[i] == '/':
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(y // x)
            else:
                ans = 'error'
                stack.pop()
        elif cal[i] == '.':
            if len(stack) >= 2:
                ans = 'error'
            elif len(stack) == 1:
                ans = stack.pop()
            else:
                ans = 'error'
        else:
            stack.append(int(cal[i]))

    print('#{} {}'.format(test_case, ans))



