import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input().split()
    stack = []
    operators = ['+', '-', '*', '/']
    ans = 0

    for i in range(len(data)-1):
        if data[i].isdigit():      # 숫자
            stack.append(data[i])
        elif data[i] in operators: # 연산자
            try:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
            except:
                ans = 'error'
                break
            else:
                if data[i] == '+':
                    stack.append(num1 + num2)
                elif data[i] == '-':
                    stack.append(num1 - num2)
                elif data[i] == '*':
                    stack.append(num1 * num2)
                elif data[i] == '/':
                    stack.append(num1 // num2)

    if not ans == 'error' and len(stack) == 1:
        ans = stack[0]
    else:
        ans = 'error'

    print('#{} {}'.format(tc, ans))

