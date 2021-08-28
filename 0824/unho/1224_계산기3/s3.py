'''
다시풀어보기
딕셔너리로 연산자 우선순위 지정
'''

import sys
sys.stdin = open('input.txt')

priority = {    # 스택 내부 순위 / 스택 외부 순위
    '(' : [0, 4],
    ')' : [0, 0],
    '*' : [3, 2],
    '/' : [3, 2],
    '+' : [2, 1],
    '-' : [2, 1],
}


for tc in range(1, 12):
    N = int(input())
    in_str = input()
    stack = []
    transform = []

    for c in in_str:
        if c.isdigit():
            transform.append(c)

        elif c in priority:
            while stack and priority[stack[-1]][0] > priority[c][1]:
                transform.append(stack.pop())
            if c == ')':
                stack.pop()
                continue
            stack.append(c)

    while stack:
        transform.append(stack.pop())

    for c in transform:
        if c.isdigit():
            stack.append(int(c))
        else:
            tmp_right = stack.pop()
            tmp_left = stack.pop()

            if c == '*':
                stack.append(tmp_left * tmp_right)
            elif c == '+':
                stack.append(tmp_left + tmp_right)

    print('#{} {}'.format(tc, stack.pop()))