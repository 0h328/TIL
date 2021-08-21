# stack

import sys
sys.stdin = open('input.txt')

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()

def is_empty():
    if len(stack) == 0:
        return True
    return False

def check_matching(data):
    for i in range(len(data)):
        if data[i] == '(':
            push(data[i])
        elif data[i] == ')':
            if is_empty() == True:
                return 0
            else:
                pop()

    for j in range(len(data)):
        if data[j] == '{':
            push(data[j])
        elif data[j] == '}':
            if is_empty() == True:
                return 0
            else:
                pop()

    if is_empty() == True:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    stack = list()
    data = input()

    print('#{} {}'.format(tc, check_matching(data)))
