import sys
sys.stdin = open('input.txt')

def push(item):
    return stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop(-1)


T = int(input())
stack = []
for tc in range(1, T+1):
    my_pip = list(input())
    cnt = 0
    idx = 0
    while idx < len(my_pip):
        if my_pip[idx:idx+2] == ['(',')']:
            idx += 2
            cnt += len(stack)
        elif my_pip[idx] == '(':
            push('(')
            idx += 1
        elif my_pip[idx] == ')':
            pop()
            idx += 1
            cnt += 1
    print('#{} {}'.format(tc, cnt))