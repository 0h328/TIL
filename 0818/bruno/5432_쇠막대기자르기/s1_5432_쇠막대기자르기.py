import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    steel = input()
    stack = []
    cut = 0                                 # 잘려서 새로 생기는 조각
    for i in range(len(steel)):
        if steel[i] == '(':
            stack.append(steel[i])          # 스택에 '(' 추가

        else:   # ')' / [i] == ')'
            if steel[i-1] == '(':           # 레이저
                stack.pop()
                cut += len(stack)           # 쌓인 스택만큼 새로운 조각 생성
            else:   # '))' / [i - 1] == ')' # 막대기 끝
                stack.pop()
                cut += 1                    # 1조각씩 추가

    print('#{} {}'.format(tc, cut))
