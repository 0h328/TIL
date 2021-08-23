import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    data = input()

    stack = [data[0]]

    for i in range(1, len(data)):
        if stack:
            if stack[-1] == data[i]:
                stack.pop()
            else:
                stack.append(data[i])

        elif not stack:
            stack.append(data[i])

    print('#{} {}'.format(test, len(stack)))
