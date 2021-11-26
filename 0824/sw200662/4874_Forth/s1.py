import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    A = input().split()
    stack = []
    for k in range(len(A)):
        if A[k] == '.':
            if len(stack) == 1:
                print('#{} {}'.format(i + 1, stack.pop()))
            else:
                print('#{} {}'.format(i + 1, 'error'))
        elif A[k].isdigit():
            stack.append(int(A[k]))
        else:
            if len(stack) < 2:
                print('#{} {}'.format(i + 1, 'error'))
                break
            else:
                temp_num2 = stack.pop()
                temp_num1 = stack.pop()
                if str(temp_num2).isdigit() and str(temp_num1).isdigit():
                    if A[k] == '+':
                        stack.append(temp_num1 + temp_num2)
                    elif A[k] == '-':
                        stack.append(temp_num1 - temp_num2)
                    elif A[k] == '*':
                        stack.append(temp_num1 * temp_num2)
                    elif A[k] == '/':
                        stack.append(temp_num1 // temp_num2)
                else:
                    print('#{} {}'.format(i + 1, 'error'))
