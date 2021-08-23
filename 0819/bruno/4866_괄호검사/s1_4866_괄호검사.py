def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()

def is_empty():
    if len(stack):
        return False
    return True

def check_matching(data):
    for i in range(len(data)):
        if data[i] == '(' or data[i] == '{':
            push(data[i])
        elif data[i] == ')':
            if stack[-1] == '{' or is_empty():
                return 0
            pop()
            # if stack[-1] == '(' and not is_empty():
            #     pop()
            # else:
            #     return 0
        elif data[i] == '}':
            if stack[-1] == '(' or is_empty():
                return 0
            pop()
            # if stack[-1] == '{' and not is_empty():
            #     pop()
            # else:
            #     return 0

    if not is_empty():
        return 0
    else:
        return 1

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    data = input()
    stack = list()
    print('#{} {}'.format(tc, check_matching(data)))
