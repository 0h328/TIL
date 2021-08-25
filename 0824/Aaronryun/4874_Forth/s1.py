import sys

sys.stdin = open('input.txt')
 # 에러 나는 경우 뽑을 숫자가 2보다 작은경우, 출력해야 하는 값이 1개보다 많은 경우
for test in range(1, 1 + int(input())):
    data = input().split()
    stack = []
    operators = {
        '+': lambda x, y: y + x,
        '-': lambda x, y: y - x,
        '*': lambda x, y: y * x,
        '/': lambda x, y: y // x,
    }
    answer = 0

    for i in data:
        if i == '.':
            answer = stack.pop()
            if stack: # 출력해야 하는 값이 2개이상일 경우
                answer = 'error'

        elif i in operators.keys(): # 키값들 중에서
            if len(stack) < 2: # 만약 뽑을 숫자가 2보다 작다면
                answer = 'error' # 에러
                break
            else:
                answer = operators[i](stack.pop(), stack.pop()) # 연산
                stack.append(answer)
        else:
            stack.append(int(i))

    print('#{} {}'.format(test, answer))
