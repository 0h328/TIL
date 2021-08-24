'''

'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    in_str = input()
    stack = []
    transform = []
    answer = []

    for c in in_str:                                # 후위표기법으로 변환
        if c.isdigit():
            transform.append(c)
        elif c == '*':
            stack.append(c)
        elif c == '+':
            if not stack:
                stack.append(c)
            else:
                while stack and stack[len(stack)-1] == '*':
                    transform.append(stack.pop())
                stack.append(c)

    while stack:
        transform.append(stack.pop())


    for e in transform:                             # 계산
        if e.isdigit():
            answer.append(e)
        elif e == '*':
            tmp_1 = answer.pop()
            tmp_2 = answer.pop()
            answer.append(int(tmp_2) * int(tmp_1))
        elif e == '+':
            tmp_1 = answer.pop()
            tmp_2 = answer.pop()
            answer.append(int(tmp_2) + int(tmp_1))


    print('#{} {}'.format(tc, *answer))