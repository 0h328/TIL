import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = input()
    stack = []
    postfix = []

    # 중위 표기법 -> 후위 표기법
    for char in data:
        if char == '*':
            stack.append(char)
        elif char == '+':
            if not stack:
                stack.append(char)
            else:
                while stack:
                    postfix.append(stack.pop())
                stack.append(char)
        else:
            postfix.append(char)
    if stack:
        while stack:
            postfix.append(stack.pop())

    # 후위 표기법 -> 계산
    for char in postfix:
        if char == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a) * int(b))
        elif char == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a) + int(b))
        else:
            stack.append(char)

    print('#{}'.format(tc), end=' ')
    print(*stack)


