import sys
sys.stdin = open('input.txt')

# 6개 맞음
# try / except

T = int(input())

for tc in range(1, T+1):
    F = list(map(str, input().split()))
    # print(F)

    stack = []
    result = []

    for i in F:
        if i in ['+', '-', '*', '/'] and len(stack) >= 2:
            b = int(stack.pop())
            a = int(stack.pop())

            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))    # 나눗셈의 경우 항상 나누어 떨어짐

        elif i in ['+', '-', '*', '/'] and len(stack) < 2:
            result.append('error')
            break

        elif i == '.' and len(stack) > 1:
            result.append('error')
            break

        elif i == '.':
            result.append(stack.pop())

        else:
            stack.append(i)

    print('#{} {}'.format(tc, *result))

    # 중간에 '.'이 나온다면?? 고려!