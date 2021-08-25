import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())                  # 수식 길이
    data = input()                    # 중위 표기법
    operator = ['(', '+', '*', ')']   # 연산자
    stack = []                        # 중위표기 -> 후위표기로 바꿀 때 연산자 관리에 필요한 stack
    postfix = []                      # 새로운 계산식 (후위 표기)

    for i in range(N):                # 중위 표현식 -> 후위 표현식 변환
        if data[i] in operator:       # 만약 연산자고
            if data[i] == '(':        # 여는 괄호를 만나면
                stack.append(data[i]) # stack에 추가
            elif data[i] == '*':      # 만약 *를 만나면
                stack.append(data[i]) # stack에 추가
            elif data[i] == '+':      # 만약 +를 만나면
                while stack[-1] != '(': # 이때 stack의 top이 여는 괄호가 아니라면
                    # 여는 괄호를 만날때까지 stack에서 계속 pop하여 postfix로 옮기고
                    postfix.append(stack.pop())
                stack.append(data[i])   # push
            else:                       # 만약 )를 만났을 때 
                while stack[-1] != '(': # stack의 top이 여는 괄호가 아니라면 
                    # (괄호가 나올때까지 pop하여 postfix로 옮기고
                    postfix.append(stack.pop())
                stack.pop()             # stack에서 최종 pop
        else:                           # 피연산자인 경우
            postfix.append(data[i])     # 바로 추가
    
    calculcation = []                   # 후위표기법 계산
    for token in postfix:
        if token == '+':                # +면 -> 2개 뽑아서 덧셈 연산 후 결과를 다시 넣고
            second = calculcation.pop()
            first = calculcation.pop()
            calculcation.append(first+second)
        elif token == '*':              # *면 -> 2개 뽑아서 곱셈 연산 후 결과를 다시 넣고
            second = calculcation.pop()
            first = calculcation.pop()
            calculcation.append(first*second)
        else:                           # 숫자면 바로 stack에 넣고(형변환)
            calculcation.append(int(token))

    ans = calculcation.pop()            # 쵲오 계산
    print('#{} {}'.format(tc, ans))


"""
중위 -> 후위 표현식 원칙
1. 숫자가 나오면 그대로 출력 
2. (이 나오면 stack에 push
3. *, /이 나오면 stack에 push 
4. +, -가 나오면 여는 괄호나 여는 괄호가 없다면 스택의 끝까지 pop하여 출력하고 +, - 연산자를 
스택에 push
5. )가 나오면 (가 나올때까지 pop하여 출력
"""