import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    in_list = input().split()
    stack = []

    for e in in_list:
        if e.isdigit():                             # 숫자라면 스택에 저장
            stack.append(int(e))

        elif e == '.':                              # 마침표일때
            if len(stack) == 1: answer = stack[-1]  # 스택에 숫자가 하나만 있으면 정답 변수에 숫자 저장
            else: answer = 'error'                  # 그 외에 모든 경우, 정답 변수에 'error' 저장
            break                                   # 반복문 종료

        elif e in ['+', '-', '*', '/']:             # 연산자일때
            if len(stack) < 2:                      # 스택에 숫자가 2개 미만일때
                answer = 'error'                    # 정답 변수에 'error' 저장
                break                               # 반복문 종료
            else:
                tmp_1 = stack.pop()                             # 뒷 숫자
                tmp_2 = stack.pop()                             # 앞 숫자
                if e == '+': stack.append(tmp_2 + tmp_1)        # 연산
                elif e == '-': stack.append(tmp_2 - tmp_1)
                elif e == '*': stack.append(tmp_2 * tmp_1)
                elif e == '/': stack.append(tmp_2 // tmp_1)


    print('#{} {}'.format(tc, answer))              # 출력