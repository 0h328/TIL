'''
스택 활용
1. 스택에 괄호를 쌓는다.
2. 한쌍의 레이저 나타나면 레이저를 뺀 스택에 남아있는 괄호만큼 카운트
3. 바로 닫는 문자 나오면 숫자 하나만 카운트 하며 여는 괄호 하나 삭제
4. 불리언 변수 하나를 넣어 레이저 바로 다음에 닫는 괄호인지 여부 판단
5. 괄호 열린게 쌓일때는 False, 레이저 방금 사용한 경우 True
'''

import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    bracket = input()
    stack = []                          # 괄호를 담을 리스트
    laser = False                       # 레이저 닫는 괄호가 바로 이전에 나왔는지 여부
    answer = 0                          # 잘린 쇠막대기 갯수

    for b in bracket:
        if b == '(':                    # 열린 괄호가 나타나면 스택에 추가, 레이저 지나지 않았으므로 False
            stack.append(b)
            laser = False
        elif b == ')':                  # 닫힌 괄호 나타나면, 스택에 있는 열린 괄호 하나 삭제
            stack.pop()
            if not laser:               # 바로 이전에 레이저 닫히는 괄호가 아니라면
                answer += len(stack)    # 현재 쇠막대기 갯수 추가
                laser = True            # 레이저가 지났으므로 True
            else:                       # 바로 이전에 레이저 닫히는 괄호였다면
                answer += 1             # 하나의 쇠막대기가 끝이 났으므로 잘린 쇠막대기 갯수 하나 추가

    print('#{} {}'.format(tc, answer))