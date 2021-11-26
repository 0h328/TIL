import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    my_string = input()
    back = ''    # 후위표기법 수식
    stack = []   # 연산자가 저장될 스택
    # icp 우선순위 : (:3 > *:2 > +:1
    # isp 우선순위 : *:2 > +:1 > (:0
    for strs in my_string:
        if strs == '(':         # 여는 괄호는
            stack.append(strs)  # 무조건 추가
        elif strs == '*':
            while stack[-1] == '*':     # *만 빼주면 됨
                back += (stack.pop())
            stack.append(strs)
        elif strs == '+':
            while stack[-1] == '+' or stack[-1] == '*':
                back += stack.pop()
            stack.append(strs)
        elif strs == ')':
            while stack[-1] != '(':     # 여는 괄호 만날 때까지 pop
                back += stack.pop()
            stack.pop()                 # 여는 괄호 버림
        else:                           # 숫자는 back에 저장
            back += strs

    while stack:            # 모든 연산자를 뒤에 갖다 붙이기
        back += stack.pop()

    result = []             # 계산을 진행하기 위한 새로운 스택
    for strs2 in back:

        if strs2 == '+':
            b = result.pop()
            a = result.pop()
            c = int(a) + int(b)
            result.append(c)
        elif strs2 == '*':
            b = result.pop()
            a = result.pop()
            c = int(a) * int(b)
            result.append(c)
        else:
            result.append(int(strs2))

    print('#{} {}'.format(tc, result[0]))