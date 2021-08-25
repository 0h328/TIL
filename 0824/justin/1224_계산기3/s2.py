# stack 내부에 있을 때 우선순위
isp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0,  # stack 내부에서 우선 순위가 가장 낮고
}

# stack 외부에 있을 때 우선순위
icp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 3,  # stack 외부에서 우선 순위가 가장 높음
}

import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    stack = []
    N = int(input())
    data = list(input())
    result = []                     # 중위 표현식 -> 후위 표현식 변경
    for token in data:
        if token.isdigit():         # 피연산자인 경우 바로 stack에 넣고
            result.append(token)
        elif token == ')':          # 닫는 괄호를 만나면
            while stack[-1] != '(': # 여는 괄호를 만날 때까지
                temp = stack.pop()  # stack에서 요소를 꺼내고
                result.append(temp) # 옮기기
            stack.pop()             # 마지막에 stack에서 pop
        elif token == '(':          # 여는 괄호면 무조건 stack에 추가
            stack.append(token)
        else:                       # 연산자인 경우는 우선 순위를 고려
            # 만약 현재 token의 우선순위가 stack의 가장 위에 있는 연산자의 우선순위 보다 높다면
            if icp[token] > isp[stack[-1]]:
                stack.append(token) # stack에 token 추가
            # stack에 있는 연산자의 우선순위가 높거나 같다면
            else:
                while icp[token] <= isp[stack[-1]]: # stack 바깥의 연산자의 우선순위가 더 높아 질때까지
                    temp = stack.pop()              # stack에서 연산자를 계속 꺼내
                    result.append(temp)             # 옮기자
                stack.append(token)                 # 최종적으로 stack에 token(연산자)를 추가하자

    calculation = []                        # 후위 표현식 계산
    for token in result:
        if token.isdigit():                 # 숫자인 경우
            calculation.append(token)       # 바로 추가하고
        else:                               # 연산자인 경우
            second = int(calculation.pop()) # 2개의 값을 뽑아서
            first = int(calculation.pop())
            if token == '+':                # +, -, /, * 연산 후
                temp = first + second
            elif token == '-':
                temp = first - second
            elif token == '/':
                temp = first / second
            else:
                temp = first * second
            calculation.append(temp)        # 결과를 stack에 추가

    ans = calculation.pop()
    print('#{} {}'.format(tc, ans))