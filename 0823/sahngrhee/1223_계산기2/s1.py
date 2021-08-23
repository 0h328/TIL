import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = input()
    data = input() # 중위 표기식
    stack = []
    data_2 = ''
    #1. 중위 표현식 -> 후위 표현식

    for char in data:
        if char == '*':
            stack.append(char)
        elif char == '+':
            # stack.append(char)
            # 이 경우 고려해야 할 사항?
            # stack이 비어있는지 여부 판단 & stack의 가장 위 (top)가 * 연산자인지 확인
            if len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1] == '*':
                    while stack:
                        data_2 += stack.pop()
                    stack.append(char)
                else:
                    while stack:
                        data_2 += stack.pop()
                    stack.append(char)
        else:
            data_2 += char
    while stack:
        data_2 += stack.pop()

    #2. 후위 표현식 -> 계산

    for char in data_2:
        if char == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
        elif char == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        else:
            stack.append(int(char))

    ans = stack.pop()
    print('#{} {}'.format(test_case, ans))