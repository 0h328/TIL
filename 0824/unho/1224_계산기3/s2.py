'''
딕셔너리로 연산자 우선순위 지정하여 풀기
'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 12):
    priority = {
        # 연산자 : [스택 밖에서 우선순위, 스택 내부 우선순위]
        '(' : [4, 0],
        ')' : [0],
        '*' : [2, 3],
        '/' : [2, 3],
        '+' : [1, 2],
        '-' : [1, 2],
    }

    N = int(input())
    in_str = input()
    stack = []
    transform = []

    for c in in_str:
        if c.isdigit():
            transform.append(c)

        elif c in priority:                                             # 연산자이면
            while stack and priority[c][0] < priority[stack[-1]][1]:    # 스택이 비어있지 않고, 우선순위 비교하여 내부 우선순위보다 낮으면
                transform.append(stack.pop())                           # 하나 pop하여 변경 결과값에 저장
            if c == ')':                                                # 닫는 괄호이면
                stack.pop()                                             # 여는 괄호 삭제
                continue
            stack.append(c)                                             # 연산자 스택에 추가

    while stack:
        transform.append(stack.pop())


    for c in transform:                             # 연산
        if c.isdigit():                             # 숫자라면
            stack.append(int(c))                    # 스택에 정수형으로 값 추가
        else:
            tmp_right = stack.pop()                 # 연산할 값을 뽑아옴
            tmp_left = stack.pop()
            if c == '*':                            # 연산 수행 후 연산 결과를 스택에 저장
                stack.append(tmp_left * tmp_right)
            elif c == '+':
                stack.append(tmp_left + tmp_right)

    print('#{} {}'.format(tc, stack.pop()))