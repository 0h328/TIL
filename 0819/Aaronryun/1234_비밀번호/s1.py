import sys
sys.stdin = open('input.txt')

for test in range(1,11):
    N, data = input().split()

    stack = [data[0]]
    for i in range(1,len(data)):
        if stack:
            if stack[-1] == data[i]:
                stack.pop()

            else:
                stack.append(data[i])

        elif not stack:
            stack.append(data[i])
    answer = ''.join(stack)
    print('#{} {}'.format(test,answer))