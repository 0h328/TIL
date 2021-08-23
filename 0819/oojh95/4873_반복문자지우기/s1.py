import sys
sys.stdin = open('input.txt')
def push(item):
    stack.append(item)
def pop():
    if is_empty():
        return False
    else:
        return stack.pop()
def is_empty():
    if len(stack):
        return False
    return True
def check(data):
    i = 0
    while i < len(data):
        if is_empty():
            push(data[i])
        elif stack[-1] == data[i]:
            pop()
        else:
            push(data[i])
        i += 1

T = int(input())
for test_case in range(1, T+1):
    data = input()
    stack = []
    check(data)
    print('#{} {}'.format(test_case, len(stack)))