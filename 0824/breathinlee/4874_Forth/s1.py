import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    data = input().split()     # 후위표기법
    stack = []

    # 10 2 + 3 4 + * .
    # isp = {')' : -, '*, /' : 2, '+, -' : 1, '(' : 0}
    # icp = {')' : -, '*, /' : 2, '+, -' : 1, '(' : 3}

    for char in data:
        if char.isdigit():          # 숫자는 스택에 넣는다.
            stack.append(char)
        elif char == '.':           # '.'은 스택에서 숫자를 꺼내 출력한다.
            if len(stack) == 1:
                print('#{} {}'.format(tc, *stack))
            else:
                print('#{} {}'.format(tc, 'error'))
        else:                       # 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
            if len(stack) == 1 or len(stack) == 0:
                print('#{} {}'.format(tc, 'error'))
                break
            else:
                a = stack.pop()
                b = stack.pop()
                if char == '*':
                    stack.append(int(b) * int(a))
                elif char == '/':
                    stack.append(int(b) // int(a))
                elif char == '+':
                    stack.append(int(b) + int(a))
                else:
                    stack.append(int(b) - int(a))
