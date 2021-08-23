def push(item):
    stack.append(item)

def pop():
    return stack.pop()

def is_empty():
    return not bool(stack)

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    for d in data:
        if d == '(':
            push(d)
        elif not is_empty() and d == ')':
            pop()
        elif is_empty() and d == ')':
            return False

    return is_empty()

import sys
sys.stdin = open('input.txt')
stack = list() # []
data = input()
data2 = input()

print(check_matching(data))  # True
stack = []                   # stack initalize
print(check_matching(data2)) # False