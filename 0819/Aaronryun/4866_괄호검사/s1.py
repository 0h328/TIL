import sys

sys.stdin = open('input.txt')

for test in range(int(input())):
    data = input()

    stack = []
    answer = 1
    for i in data:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == ')' or i == '}':
            if not stack:
                answer = 0
                break
            P = stack.pop()
            if i == ')' and P != '(':
                answer = 0
            elif i == '}' and P != '{':
                answer = 0

    if stack:
        answer = 0

    print('#{} {}'.format(test + 1, answer))
