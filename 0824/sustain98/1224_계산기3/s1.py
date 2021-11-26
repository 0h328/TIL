import sys
sys.stdin = open('input.txt')

priority = {'+': 0, '*': 1, '(': -1, ')': -1}
for idx in range(1, 11):
    length = int(input())
    stack = []
    s = input()
    new_s = ''
    for i in s:
        if i.isdigit():
            new_s += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                new_s += stack.pop()
            stack.pop()
        else:
            while stack and priority[stack[-1]] >= priority[i]:
                new_s += stack.pop()
            stack.append(i)
    while stack:
        new_s += stack.pop()

    #후위 표기식 -> 계산
    for i in new_s:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '*':
                stack.append(b*a)
            else:
                stack.append(b+a)
    print('#{} {}'.format(idx, stack.pop()))
