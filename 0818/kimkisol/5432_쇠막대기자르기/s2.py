import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    case = input()
    case_list = list(case)
    stack = []
    temp = []
    idx = 0
    result = 0
    while idx < len(case):
        if case[idx:idx + 2] == '()':
            stack.append('*')
            idx += 2
            continue
        elif case[idx] == '(':
            stack.append('(')
        elif case[idx] == ')' and '(' in stack:
            result += 1
            while stack[-1] != '(':
                temp.append(stack.pop())
                result += 1
            stack.pop()
            while temp != []:
                stack.append(temp.pop())
        idx += 1
    print('#{} {}'.format(t, result))
