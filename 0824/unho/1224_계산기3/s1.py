import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    in_str = input()
    stack = []
    transform = ''

    for c in in_str:
        if c.isdigit():                     # 숫자이면 새로운 문자열에 이어 붙임
            transform += c

        else:                               # 그 외 (연산자 및 괄호)
            while c == '*' and stack and stack[-1] == '*':
                transform += stack.pop()
            while (c == '+' or c == ')') and stack and stack[-1] != '(':    # 곱하기, 여는괄호는 무조건 추가 / 더하기, 닫는괄호는 우선순위 높거나 같은거 빼서 새로운 문자열에 이어 붙임
                transform += stack.pop()
            if c == ')':                    # 닫는 괄호라면, 여는 괄호 삭제하고, 스택에 추가는 안하므로 컨티뉴로 통과
                stack.pop()
                continue
            stack.append(c)                 # 스택에 현재 연산자 추가

    while stack:                            # 스택에 남은 연산자 있으면 모두 추가
        transform += stack.pop()

    print(transform)

    for c in transform:                     # 연산
        if c.isdigit():                     # 숫자라면
            stack.append(int(c))            # 스택에 정수형으로 값 추가
        else:
            tmp_right = stack.pop()         # 연산할 값을 뽑아옴
            tmp_left = stack.pop()
            if c == '*':                    # 연산 수행 후 연산 결과를 스택에 저장
                stack.append(tmp_left * tmp_right)
            elif c == '+':
                stack.append(tmp_left + tmp_right)

    print('#{} {}'.format(tc, stack.pop()))