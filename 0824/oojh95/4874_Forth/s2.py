import sys
sys.stdin = open('input.txt')

def check(arr):
    for i in range(len(arr)):
        if arr[i] == '.':   # 문장 끝일때 처리 방법
            if len(stack) == 1: # stack에 수가 남아있으면 결과값 출력
                return stack.pop()
            else:   # 없으면 error
                return 'error'
        elif arr[i] == '+' and len(stack) >= 2:
            stack.append(stack.pop() + stack.pop())
        elif arr[i] == '-' and len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif arr[i] == '*' and len(stack) >= 2:
            stack.append(stack.pop() * stack.pop())
        elif arr[i] == '/' and len(stack) >= 2: # / -는 순서 중요.
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
        elif arr[i] == '+' or arr[i] == '-' or arr[i] == '*' or arr[i] == '/':  #연산자를 받았으나 피연산자가 2개보다 적을때는 error
            return 'error'
        else:
            stack.append(int(arr[i]))


T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []

    print('#{} {}'.format(tc, check(arr)))