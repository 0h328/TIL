import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    code = input()
    stack = []
    for char in code:
        if char == '{' or char == '(':           # 여는 괄호를 만나면
            stack.append(char)                   # 일단 stack에 넣자
        elif char == '}':                          # 만약 닫는 중괄호를 만나면
            if len(stack) and stack[-1] == '{':  # 이때 stack이 비어있지 않고 stack의 가장 위가 닫는 중괄호면
                stack.pop()                      # 꺼내자 (매칭)
            else:                                # 아닌 경우
                stack.append(char)               # stack에 닫는 중괄호 추가
        elif char == ')':                          # 만약 닫는 소괄호를 만나면
            if len(stack) and stack[-1] == '(':  # stack이 비어있지 않고 stack의 가장 위가 여는 소괄호면
                stack.pop()                      # stack에서 괄호 꺼내고
            else:                                # stack이 비어있지 않거나 stack의 가장 위가 여는 소괄호가 아니면
                stack.append(char)               # stack에 ) 추가
    ans = 0 if len(stack) else 1                 # 짝을 전부 찾았으면(stack이 비어있음) 0 아니면 1
    print('#{} {}'.format(tc, ans))