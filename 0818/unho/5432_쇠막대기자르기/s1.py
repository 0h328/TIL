import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    bracket = input()
    stack = []
    laser = False                       # 직전에 레이저였는지 여부
    answer = 0

    for b in bracket:
        if b == '(':                    # 여는 괄호면 스택에 추가, 레이저가 아니므로 False
            stack.append(b)
            laser = False
        elif b == ')':                  # 닫는 괄호면
            stack.pop()                 # 여는 괄호 하나 삭제
            if not laser:               # 직전에 레이저가 아니였으면 지금까지 스택에 쌓인 갯수 추가
                answer += len(stack)
                laser = True
            elif laser:                 # 직전에 레이저였다면 쇠막대기 하나 사라지므로 하나만 증가
                answer += 1


    print('#{} {}'.format(tc, answer))