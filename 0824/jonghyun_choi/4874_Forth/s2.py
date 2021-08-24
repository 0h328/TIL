import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    data = list(map(str,input().split()))

    stack = []

    for i in range(len(data)):
        if data[i].isdecimal():
            stack.append(data[i])
        else:
            if data[i] != '.' and len(stack) < 2:
                print('#{} {}'.format(case + 1, 'error'))
                break
            elif data[i] == '.':
                if len(stack) > 1:
                    print('#{} {}'.format(case + 1, 'error'))
                    break
                else:
                    print('#{} {}'.format(case + 1, ''.join(map(str, stack))))

            else:
                if data[i] == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a) * int(b))
                elif data[i] == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b) // int(a))
                elif data[i] == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a) + int(b))
                elif data[i] == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b) - int(a))

