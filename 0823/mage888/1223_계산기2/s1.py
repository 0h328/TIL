import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = input()
    stack = []
    postfix = []

#1. 중위 표현식 -> 후위 표현식

    for char in data:
        if char == '*' and not stack:
            stack.append(char)
        elif char == '*' and stack:
            if stack[-1] == '*':
                while stack[-1] != '*':
                    postfix.append(stack.pop())
                    if not stack:
                        break
                stack.append(char)
            else:
                stack.append(char)
        elif char == '+' and not stack:
            stack.append(char)
        elif char == '+' and stack:
            if stack[-1] == '*' or stack[-1] == '+':
                while stack[-1] != '*' or stack[-1] != '+':
                    postfix.append(stack.pop())
                    if not stack:
                        break
                stack.append(char)
            else:
                stack.append(char)
        else:
            postfix.append(char)
    if stack:
        while stack:
            postfix.append(stack[-1])
            stack.pop()

    for char in postfix:
        if char in '0123456789':
            stack.append(char)
        elif char == '+' and len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()
            c = int(a) + int(b)
            stack.append(c)
        elif char == '*' and len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()
            c = int(a) * int(b)
            stack.append(c)

    print('#{}'.format(tc), end=' ')
    print(*stack)

# 이 경우 고려해야 할 사항?
# stack이 비어있는지 여부 판단 & stack의 가장 위(top)가 * 연산자인지 확인

