import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    formula = input().split()
    stack = []

    try:
        for i in range(len(formula)):
            if formula[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif formula[i] == '/':
                stack.append(stack.pop(-2) // stack.pop())
            elif formula[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif formula[i] == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif formula[i] == '.':
                if i != len(formula) - 1 or len(stack) != 1:
                    print('#{} error'.format(t))
                    break
                else:
                    print('#{} {}'.format(t, stack[0]))
            else:
                stack.append(int(formula[i]))
    except Exception:
        print('#{} error'.format(t))
