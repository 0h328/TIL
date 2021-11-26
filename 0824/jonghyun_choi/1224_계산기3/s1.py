import sys
sys.stdin = open('input.txt')

for case in range(10):
    length = int(input())
    data = list(input())
    stack = []
    ans = ''
    for i in range(len(data)):
        if data[i].isdecimal():
            ans += data[i]
        else:
            if data[i] == '(':
                stack.append(data[i])
            elif data[i] == ')':
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()

            elif data[i] == '*':
                if '(' in stack:
                    while stack[-1] != '(' and stack[-1] == '*':
                        ans += stack.pop()
                    stack.append(data[i])
                else:
                    while stack and stack[-1] == '*':
                        ans += stack.pop()
                    stack.append(data[i])
            elif data[i] == '+':
                if '(' in stack:
                    while stack[-1] != '(':
                        ans += stack.pop()
                    stack.append(data[i])
                else:
                    while stack:
                        ans += stack.pop()
                    stack.append(data[i])

    while stack:
        ans += stack.pop()

    for i in ans:
        if i.isdecimal():
            stack.append(i)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a) * int(b))
        elif i == '+':
            c = stack.pop()
            d = stack.pop()
            stack.append(int(c) + int(d))
    print('#{} {}'.format(case + 1, ''.join(map(str, stack))))


