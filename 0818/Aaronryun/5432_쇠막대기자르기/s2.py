import sys

sys.stdin = open('input.txt')

for test in range(1,1+int(input())):

    data = input()
    stack = []
    answer = 0

    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])
        elif data[i] == ')':
            if data[i-1] == '(': # 레이저
                stack.pop()
                answer += len(stack)

            else:
                stack.pop(0)  #
                answer += 1

    print('#{} {}'.format(test, answer))
