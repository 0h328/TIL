import sys
sys.stdin = open('input.txt')

def check(arr):
    for i in range(len(arr)):
        if arr[i] == '.' and len(stack) == 1:
            return stack.pop()
        elif arr[i] == '.':
            return 'error'
        elif arr[i] == '+' and len(stack) >= 2:
            stack.append(stack.pop() + stack.pop())
        elif arr[i] == '-' and len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif arr[i] == '*' and len(stack) >= 2:
            stack.append(stack.pop() * stack.pop())
        elif arr[i] == '/' and len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
        elif arr[i] == '+' or arr[i] == '-' or arr[i] == '*' or arr[i] == '/':
            return 'error'
        else:
            stack.append(int(arr[i]))


T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []

    print('#{} {}'.format(tc, check(arr)))