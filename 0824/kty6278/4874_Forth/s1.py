import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    data = list(map(str, input().split()))
    stack = []

    for n in data:
        if n == '.':
            if len(stack) == 1:                          # 마지막이 . 인 경우 판단
                break
            else:                                        # 연산 필요한데, 숫자 두개인 경우
                stack = ['error']
                break

        if n == '*' or n == '+' or n == '/' or n == '-': # 숫자가 아닌 연산기호
            if len(stack) > 1:                           # 숫자가 두개 존재하는가?
                a = int(stack.pop())
                b = int(stack.pop())
                if n == '*':
                    stack.append(b * a)
                if n == '+':
                    stack.append(b + a)
                if n == '/':                             # pop 순서 주의
                    stack.append(b // a)
                if n == '-':                             # pop 순서 주의
                    stack.append(b - a)
            else:                                        # 숫자인 경우
                stack = ['error']
                break
        else:
            stack.append(int(n))

    if len(stack) >= 2:                                  # 연산이 없이 숫자만 두개 남은 경우
        stack = ['error']

    print('#{} {}'.format(tc + 1, *stack))