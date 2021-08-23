import sys
sys.stdin = open('input.txt')

for test in range(10):
    N = input()
    data = input()
    stack = []
    temp = ''
    result = []

    # 1. 중위 표현식 -> 후위 표현식
    for char in data:
        if char == '*':  # '*'는 우선순위가 높으므로 그냥 추가
            stack.append(char)
        elif char == '+':
            while stack:  # '+'가 들어오면 stack에 있는 것들 전부 뱉음
                temp += stack.pop()
            stack.append(char)  # '+' 추가
        else:
            temp += char

    while stack:  # stack에 남아있는 것들 모두 추가
        temp += stack.pop()

    # 2. 후위 표현식 -> 계산
    for char in temp:
        if char == '*':  # '*'인 경우(숫자 2개 꺼내서 곱하고 다시 넣음)
            num1 = result.pop()
            num2 = result.pop()
            result.append(num1*num2)
        elif char == '+':  # '+'인 경우(숫자 2개 꺼내서 더하고 다시 넣음)
            num1 = result.pop()
            num2 = result.pop()
            result.append(num1+num2)
        else:
            result.append(int(char))

    print('#{} {}'.format(test+1, result[0]))
