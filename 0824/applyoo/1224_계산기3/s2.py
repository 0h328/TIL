import sys
sys.stdin = open('input.txt')

for test in range(10):
    N = int(input())
    arr = list(map(str, input()))
    postfix = ''  # 후위 표기식 저장
    stack, result = [], []  # 연산자 저장 / 후위 연산 결과 저장
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}  # 스택 밖에서 우선순위
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}  # 스택 안에서 우선순위

    for word in arr:
        if word.isdigit():  # 숫자인 경우
            postfix += word
        elif word == ')':  # 괄호인 경우
            while stack and stack[-1] != '(':  # 스택의 top이 '('일때까지 반복하고, '('는 pop
                postfix += stack.pop()
            stack.pop()
        else:  # 연산자인 경우
            while stack and icp[word] <= isp[stack[-1]]:  # 스택안의 우선순위가 크거나 같으면 계속 pop
                postfix += stack.pop()
            stack.append(word)  # 연산자 push

    while stack:  # 남아있는 연산자가 있다면 모두 pop
        postfix += stack.pop()

    for char in postfix:
        if char == '*':  # '*'인 경우(숫자 2개 꺼내서 곱하고 다시 넣음)
            result.append(result.pop() * result.pop())
        elif char == '+':  # '+'인 경우(숫자 2개 꺼내서 더하고 다시 넣음)
            result.append(result.pop() + result.pop())
        else:
            result.append(int(char))

    print('#{} {}'.format(test + 1, result[0]))
