import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = input()
    stack = []
    postfix = []

    for char in data:
        if char == '(':
            stack.append(char)
        elif char == '*':
            stack.append(char)
        elif char == '+':
            if stack[-1] == '*':
                while stack[-1] == '*':
                    postfix.append(stack.pop())
                stack.append(char)
            elif stack[-1] == '+':
                while stack[-1] == '+':
                    postfix.append(stack.pop())
                stack.append(char)
            else:
                stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif char.isdigit():
            postfix.append(int(char))

    for char in postfix:
        if char == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif char == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        else:
            stack.append(char)


    print('#{}'.format(tc), end=' ')
    print(*stack)