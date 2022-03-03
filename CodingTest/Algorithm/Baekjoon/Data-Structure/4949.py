import sys
sys.stdin = open('input.txt')

while True:
    stack = []
    x = input()

    if x == '.':
        break

    for i in x:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break

    if stack:
        print('no')
    else:
        print('yes')
