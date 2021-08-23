# 도둑잡기 게임이 생각나는 문제
import sys
sys.stdin = open('input.txt')

T = int(input())
test_case = 1

while test_case <= T:
    input_str = list(input())
    stack = []

    for idx in range(len(input_str)):   # 문자 순회
        if not stack:                   # 스택이 비어 있으면
            stack.append(input_str[idx])
        else:                           # 스택이 차 있으면
            if input_str[idx] == stack[-1]:     # 스택 마지막과 순회하는 문자가 같으면
                stack.pop()             # 빼 냅니다
            else:                       # 스택 마지막과 다르면
                stack.append(input_str[idx])    # 스택에 넣습니다

    print('#{0} {1}'.format(test_case, len(stack)))
    # break
    test_case += 1
