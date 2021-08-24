import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = input()
    data = input()
    stack = []
    data_2 = ''

    for char in data:
        if char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                data_2 += stack.pop()
            stack.pop()
        elif char == '+':
            if len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.append(char)
                else:
                    while stack[-1] != '(':
                        data_2 += stack.pop()
                    stack.append(char)
                # if stack[-1] == '-':
                #     while stack[-1] != '(':
                #         data_2.append(stack.pop())
                # if stack[-1] == '+':
                #     while stack[-1] != '(':
                #         data_2.append(stack.pop())
                # if stack[-1] == '*':
                #     while stack[-1] != '(':
                #         data_2.append(stack.pop())
                # if stack[-1] == '/':
                #     while stack[-1] != '(':
                #         data_2.append(stack.pop())

        elif char == '-':
            if len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.append(char)
                else:
                    while stack[-1] != '(':
                        data_2 += stack.pop()
                    stack.append(char)

        elif char == '*':
            if len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.append(char)
                elif stack[-1] == '+' or stack[-1] == '-':
                    stack.append(char)
                elif stack[-1] == '*' or stack[-1] == '/':
                    while stack[-1] != '+' and stack[-1] != '-' and stack[-1] != '(':
                        data_2 += stack.pop()
                    stack.append(char)

        elif char == '/':
            if len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.append(char)
                elif stack[-1] == '+' or stack[-1] == '-':
                    stack.append(char)
                elif stack[-1] == '*' or stack[-1] == '/':
                    while stack[-1] != '+' and stack[-1] != '-' and stack[-1] != '(':
                        data_2 += stack.pop()
                    stack.append(char)

        else:
            data_2 += char

    while stack:
        data_2 += stack.pop()

    for char in data_2:
        if char == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
        elif char == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(x * y)
        elif char == '-':
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
        elif char == '/':
            x = stack.pop()
            y = stack.pop()
            stack.append(y / x)
        else:
            stack.append(int(char))

    ans = stack.pop()
    print('#{} {}'.format(test_case, ans))