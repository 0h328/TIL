import sys
sys.stdin = open('input.txt')

def push(item):
    stack.append(item)
def pop():
    if is_empty():
        return
    else:
        return stack.pop()
def is_empty():
    if len(stack):
        return False
    return True
def check_data(data):
    for i in range(len(data)):
        if data[i] in ['(', '{']:
            push(data[i])
        elif data[i] == ')':
            if not is_empty() and stack[-1] == '(':
                pop()
            else:
                return 0
        elif data[i] == '}':
            if not is_empty() and stack[-1] == '{':
                pop()
            else:
                return 0
    if is_empty():
        return 1
    else:
        return 0

T = int(input())
for test_case in range(1, T+1):
    data = input()
    stack = []
    print('#{} {}'.format(test_case, check_data(data)))
