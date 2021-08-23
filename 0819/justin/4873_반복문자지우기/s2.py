def solve(chars):
    stack = []
    for char in chars:
        # 항상 마지막 문자를 확인
        if stack and stack[-1] == char: # stack 에 내용물이 있고, 마지막 문자가 중복이라면
            stack.pop()                 # stack에서 해당 문자 삭제
            continue                    # 현재 문자는 반복 넘어감
        stack.append(char)
    return len(stack)

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    chars = input()
    ans = solve(chars)
    print('#{} {}'.format(tc, ans))