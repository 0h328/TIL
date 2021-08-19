import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    in_str = input()
    stack = []
    answer = 1                                          # 정상이면 1, 정상이지 않으면 0

    for c in in_str:
        if c == '(' or c == '{':                        # 여는 괄호면 스택에 추가
            stack.append(c)
        elif c == ')' or c == '}':                      # 닫는 괄호일때
            if stack:                                   # 스택에 값이 있다면
                if c == ')' and stack[-1] == '(':       # 괄호 짝이 맞으면 여는 괄호 삭제
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:                                   # 괄호 짝이 맞지 않으면 비정상
                    answer = 0
                    break
            else:                                       # 스택이 비어있는데 닫는 괄호가 나오면 비정상
                answer = 0
                break

    if stack:                                           # 스택에 값이 남아있다면 비정상
        answer = 0

    print('#{} {}'.format(tc, answer))