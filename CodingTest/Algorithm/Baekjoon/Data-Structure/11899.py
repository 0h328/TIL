import sys
sys.stdin = open('input.txt')

x = input()
stack = []
cnt = 0

for i in range(len(x)):
    if x[i] == '(':
        stack.append(x[i])
    elif x[i] == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            cnt += 1

print(cnt + len(stack))