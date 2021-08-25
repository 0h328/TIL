import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    data = input()
    stack_operator = []
    stack_ret = []
    # isp = {')' : -, '*, /' : 2, '+, -' : 1, '(' : 0}
    # icp = {')' : -, '*, /' : 2, '+, -' : 1, '(' : 3}

    # 후위표기법으로
    for char in data:
        if char.isdigit():
            stack_ret.append(char)
        elif char == '(':
            stack_operator.append(char)
        elif char == ')':
            while stack_operator[-1] != '(':
                stack_ret.append(stack_operator.pop())
            stack_operator.pop()
        elif char == '*':
            while stack_operator[-1] == '*':
                stack_ret.append(stack_operator.pop())
            stack_operator.append(char)
        else:
            if len(stack_operator) == 0:
                stack_operator.append(char)
            else:
                while stack_operator[-1] == '+' or stack_operator[-1] == '*':
                    stack_ret.append(stack_operator.pop())
                stack_operator.append(char)

    while stack_operator:    # 남은 연산자 처리
        stack_ret.append(stack_operator.pop())

    # 계산
    calculation = []
    for char in stack_ret:
        if char == '*' or char == '+':                 # 연산자의 경우 피연산자를 두번 pop()하여 연산
            a = calculation.pop()
            b = calculation.pop()
            if char == '*':
                calculation.append(int(b) * int(a))            # 연산 결과를 다시 push
            else:
                calculation.append(int(b) + int(a))            # 연산 결과를 다시 push
        else:
            calculation.append(char)

    print('#{} {}'.format(tc, *calculation))