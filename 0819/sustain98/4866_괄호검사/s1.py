import sys
sys.stdin = open('input.txt')

t = int(input())
for num in range(1, t+1):
    s = input()
    stack = []
    d = {'{': '}', '(': ')'}
    top = -1
    res = 1
    for i in s:
        if i in '{(':
            stack.append(i)
            top += 1
        elif i in '})':
            if top > -1 and i == d[stack[top]]:
                stack.pop(top)
                top -= 1
            else:
                res = 0
                break
    if stack:
        res = 0

    print('#{} {}'.format(num, res))


