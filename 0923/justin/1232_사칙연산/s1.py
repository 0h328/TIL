def calc(op, left, right):
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        result = left / right
    return result

import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())            # 정점의 개수
    stack = []                  # 스택을 활용하여 연산자의 노드 번호 저장
    operator = [''] * (N+1)     # 연산자(operator)
    operand = [0] * (N+1)       # 피연산자(operand)
    first_child  = [0] * (N+1)  # 왼쪽 자식
    second_child = [0] * (N+1)  # 오른쪽 자식

    for i in range(N):
        """
        정점이 피연산자면 [정점 번호, 양의 정수]
        정점이 연산자면 [정점 번호, 연산자, 연산자를 기준으로 왼쪽, 오른쪽 자식의 정점 번호] 
        """
        temp = list(input().split())  # 정점 정보
        idx = int(temp[0])            # 정점 번호 (노드 번호 -> idx로 활용)

        if temp[1] == '+' or temp[1] == '-' or temp[1] == '*' or temp[1] == '/':    # 연산자이면
            operator[idx] = temp[1]                                                 # 연산자를 idx에 넣고
            first_child[idx] = int(temp[2])                                         # 왼쪽 자식을 왼쪽에
            second_child[idx] = int(temp[3])                                        # 오른쪽 자식을 오른쪽에 넣자
            stack.append(idx)                                                       # idx를 stack에 push
        else:                                                                       # 피연산자(숫자)면
            operand[idx] = int(temp[1])                                             # 해당 숫자를 넣자

    while stack:                        # 스택 이용해서 연산자를 숫자로 계산(후위 표현식 -> 계산 작업)
        idx = stack.pop()               # stack에서 하나씩 값을 꺼내서 연산 수행
        operand[idx] = calc(            # 피연산자 1 연산자 피연산자 2의 결과 -> operand[idx]
            operator[idx],              # 연산자
            operand[first_child[idx]],  # 피연산자 1
            operand[second_child[idx]]  # 피연산자 2
        )

    print('#{} {}'.format(tc, int(operand[1])))