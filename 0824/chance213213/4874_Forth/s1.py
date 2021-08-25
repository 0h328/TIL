import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(input().split())
    stack = []
    top = -1


    try:
        for chr in data:
            if chr == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif chr == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif chr == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif chr == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)
            elif chr == '.':
                if len(stack) == 1:
                    ans = stack.pop()
                    print('#{} {}'.format(tc, ans))
                else:
                    print('#{} error'.format(tc))
                    break
            else:
                stack.append(int(chr))



    except IndexError:
        print('#{} error'.format(tc))