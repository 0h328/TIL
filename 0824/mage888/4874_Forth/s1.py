import sys
sys.stdin = open('input.txt')

def Forth():

    for char in data:
        if char.isdigit():
            stack.append(int(char))
        elif char == '*':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            else:
                return 'error'
        elif char == '+':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            else:
                return 'error'
        elif char == '-':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            else:
                return 'error'
        elif char == '/':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)            # '//' 한 이유 : 나눗셈은 항상 나눠 떨어진다.
            else:
                return 'error'
        elif char == '.':
            if len(stack) == 1:                 # 길이가 1과 그렇지 않은 것을 나누지 않으면 tc 틀림 발생
                return stack.pop()
            else:
                return 'error'

T = int(input())
for tc in range(1, T+1):
    data = input().split()
    stack = []

    print('#{} {}'.format(tc, Forth()))


