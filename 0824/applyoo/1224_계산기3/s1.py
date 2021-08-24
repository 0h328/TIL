import sys
sys.stdin = open('input.txt')

for test in range(10):
    N = int(input())
    data = list(map(str, input()))
    temp = ''  # 후위 표기식 저장
    stack, result = [], []  # 연산자 저장 / 후위 연산 결과 저장

    for word in data:
        if word == '*':  # 곱셈인 경우 push
            stack.append(word)
        elif word == '+':  # 덧셈인 경우 스택의 top이 '('일때까지 pop, 이후 push
            while stack and stack[-1] != '(':
                temp += stack.pop()
            stack.append(word)
        elif word == '(':  # '('는 push
            stack.append('(')
        elif word == ')':  # ')'는 스택의 top이 '('일때까지 pop, 이후 '(' pop
            while stack[-1] != '(':
                temp += stack.pop()
            stack.pop()
        else:  # 숫자인 경우
            temp += word

    while stack:  # 남아있는 연산자가 있다면 모두 pop
        temp += stack.pop()

    for char in temp:
        if char == '*':  # '*'인 경우(숫자 2개 꺼내서 곱하고 다시 넣음)
            num1 = result.pop()
            num2 = result.pop()
            result.append(num1 * num2)
        elif char == '+':  # '+'인 경우(숫자 2개 꺼내서 더하고 다시 넣음)
            num1 = result.pop()
            num2 = result.pop()
            result.append(num1 + num2)
        else:
            result.append(int(char))

    print('#{} {}'.format(test + 1, result[0]))
