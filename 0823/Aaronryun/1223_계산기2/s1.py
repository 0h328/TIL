import sys

sys.stdin = open('input.txt')

for test in range(1, 11):
    N = int(input())
    data = input()
    stack = []

    answer = ''
    # *일때는 연산자를 스택에 더하고 +가 등장하면 연산자를 모두 문자열에 더하고 피연산자는 바로 문자열에 더한다.
    for i in data:
        if i == '*':
            stack.append(i)
        elif i == '+':
            while stack:
                answer += stack.pop()
            stack.append(i)
        else:
            answer += i

    while stack:  # 남은 스택에 있는거 다 더한다
        answer += stack.pop()

    result = []
    for i in answer:  # 숫자는 다 더하고 *일때는 뽑아서 곱하고 +일떄는 뽑아서 더하고
        if i == '*':
            a = result.pop()
            b = result.pop()
            c = b * a
            result.append(c)

        elif i == '+':
            a = result.pop()
            b = result.pop()
            c = b + a
            result.append(c)

        else:
            result.append(int(i))

    print('#{} {}'.format(test, *result))
    print('#{}'.format(test), *result)
