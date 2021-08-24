'''
1. 스택을 이용하여 후위표기법으로 변환
- 받아온 문자열을 한 글자씩 순환하면서 연산자는 스택에 담고, 비연산자는 새로운 문자열에 담는다
- 비연산자를 스택에 넣을때, 스택에 우선순위가 더 높은게 있다면, pop을 해서 문자열에 붙이고 스택에 비연산자 추가
- 우선순위가 동등하거나 낮으면 그냥 추가
- 문자열을 모두 순환하면, 스택에 남아있는 연산자들을 모두 새로운 문자열 뒤에 붙인다.

2. 후위표기법을 이용하여 계산
- 후위표기법으로 전환한 문자열의 앞부분부터 순환
- 비연산자를 스택에 넣는다.
- 연산자를 만나면 스택에서 두개의 피연산자를 빼낸다.
- 나누기나 빼기시에 순서가 중요하므로 먼저 뺀 숫자가 뒤로 가게 한다.
- 연산한 숫자는 다시 스택에 추가한다.
- 문자열 끝까지 반복
'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    in_str = input()
    stack = []
    trans = ''

    for c in in_str:                                        # 후위표현식으로 변환
        if c.isdigit():                                     # 숫자면 문자열 뒤에 붙임
            trans += c
        elif c in ['*', '+']:                               # 연산자이면
            while c == '+' and stack:                       # + 연산자이고, 스택이 비어있지 않고, top이 우선순위가 더 크면
                trans += stack.pop()                        # 문자열 뒤에 연산자 붙임
            stack.append(c)                                 # 스택에 추가

    while stack:                                            # 남은 연산자 모두 뒤에 붙임
        trans += stack.pop()

    print(trans)

    for c in trans:                                         # 문자 하나하나 순환
        if c.isdigit():                                     # 숫자면 스택에 추가
            stack.append(int(c))
        elif c in ['*', '+']:                               # 연산자이면
            tmp_1 = stack.pop()                             # 숫자 두개 꺼내옴
            tmp_2 = stack.pop()
            if c == '*':                                    # 연산 후 스택에 다시 추가
                stack.append(tmp_2 * tmp_1)
            elif c == '+':
                stack.append(tmp_2 + tmp_1)


    print('#{} {}'.format(tc, stack[0]))                    # 출력




# 처음 코드 작성
# import sys
# sys.stdin = open('input.txt')
#
# for tc in range(1, 11):
#     N = int(input())
#     in_str = input()
#     stack = []
#     transform = []
#     answer = []
#
#     for c in in_str:                                # 후위표기법으로 변환
#         if c.isdigit():
#             transform.append(c)
#         elif c == '*':
#             stack.append(c)
#         elif c == '+':
#             if not stack:
#                 stack.append(c)
#             else:
#                 while stack and stack[len(stack)-1] == '*':
#                     transform.append(stack.pop())
#                 stack.append(c)
#
#     while stack:
#         transform.append(stack.pop())
#
#
#     for e in transform:                             # 계산
#         if e.isdigit():
#             answer.append(e)
#         elif e == '*':
#             tmp_1 = answer.pop()
#             tmp_2 = answer.pop()
#             answer.append(int(tmp_2) * int(tmp_1))
#         elif e == '+':
#             tmp_1 = answer.pop()
#             tmp_2 = answer.pop()
#             answer.append(int(tmp_2) + int(tmp_1))
#
#
#     print('#{} {}'.format(tc, *answer))