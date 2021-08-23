'''
stack
하나씩 값 넣다가 안에 값과 현재 값이 같으면 삭제
'''


import sys
sys.stdin = open('input.txt')



test_case = int(input())

for tc in range(1, test_case+1):
    in_str = input()
    stack = []

    for c in in_str:                        # 문자열 글자 반복
        if not stack or c != stack[-1]:     # 스택이 비어있거나, 스택 마지막 문자와 현재 문자가 다르면 스택에 추가
            stack.append(c)
        elif c == stack[-1]:                # 스택의 마지막 문자와 현재 문자가 같으면 삭제
            stack.pop()

    answer = len(stack)

    print('#{} {}'.format(tc, answer))