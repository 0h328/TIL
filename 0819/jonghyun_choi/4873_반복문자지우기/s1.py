import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    data = input()
    stack = []

    for i in data:
        if i not in stack:
            stack.append(i)
        elif len(stack) > 0 and  i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    print('#{} {}'.format(case + 1, len(stack)))

