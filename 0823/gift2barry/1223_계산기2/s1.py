import sys
sys.stdin = open('input.txt')


# thought process: 12분
# 먼저 중위 표기법을 후위표기법으로 바꾸자:
# # 1 피연산자는 무조건 출력
# # 2 스택이 빈 상태에서 연산자 만나면 무조건 append
# # 3 스택 안에 연산자가 현재 연산자보다 우선순위가 높으면, 스택 안에것 pop하고 출력, 현재 연산자는 stack 안에 append
# # 4 중위 표현식의 끝에 도달하면 스택 안에 남아있는 모든 연산자를 출력
# 다음으로 후위 표기법을 계산하자:
# # 1 피연산자는 무조건 stack 에 push
# # 2 연산자 만나면, 피연산자 두개 pop, (두번째 pop 값) (연산자) (위에 pop 값) 순으로 계산 후
# # 3 결과 값을 다시 stack에 push
# # 4 후위 표기식의 끝에 도달하면, 스택 안에 남아있는 피연산자를 출력 = 계산값

# 문제 해결 실패
# # 원인 : 불명
# # thought process 그대로 구현에는 성공, 하지만 SWEA 에서 원하는 output 값과는 다르다. 뭐가 잘못된거지

for tc in range(1, 11):

    N = int(input())
    my_str = input()    # 인풋 중위 표기법
    stack = []          # 스택 초기화
    temp = ''           # 후위 표기법을 담을 임시 문자열 생성

    # 중위 표기법을 후위표기법으로 변환 작업
    for i in range(N):                      # 인풋 중위 표기법 문자열 길이만큼 반복
        if my_str[i] in '0123456789':       # 피연산자일때
            temp += my_str[i]               # 해당 문자 temp 에 할당
        elif len(stack) == 0:                   # 빈 stack 일때
            stack.append(my_str[i])             # 연산자를 무조건으로 push()
        elif len(stack) != 0 and stack[-1] == '+':              # stack 안에 연산자가 있고, top 이 '+' 일때
            stack.append(my_str[i])                             # 현재 i 에 해당하는 연산자 push()
        elif len(stack) != 0 and stack[-1] == '*' and my_str[i] == '+':     # stack 안에 연산자가 있고, top 이 현재 i에 해당하는 연산자보다 우선순위가 높을때,
            temp += stack.pop()                                             # 현재 top 출력
            stack.append(my_str[i])                                         # 현재 i 해당 연산자 push()
        elif len(stack) != 0 and stack[-1] == '*' and my_str[i] == '*':     # stack 안에 연산자가 있고, top 이 현재 i에 해당하는 연산자와 우선순위가 같은 경우,
            stack.append(my_str[i])                                         # 현재 i 해당 연산자 push()

    if len(stack) != 0:                             # 루프가 중위 표현식의 끝에 도달했는데도 stack 안에 연산자들이 남아있다면,
        for i in range(len(stack)):                 # 모든 연산자들 pop() 해서
            temp += stack.pop()                     # temp에 할당, stack 을 비운다
    # print(temp)
    # print(stack)

    # 후위 표기법으로 계산 작업
    for i in range(len(temp)):                # temp 의 문자열 길이만큼 반복
        if temp[i] in '0123456789':           # 피 연산자일경우
            stack.append(int(temp[i]))             # stack에 push()
        elif temp[i] == '+':                  # '+' 연산자일 경우
            b = stack.pop()             # stack 안의 두개의 피연산자 pop()
            a = stack.pop()
            calc = a + b                      # 해당 연산자로 두개의 피 연산자 계산
            stack.append(calc)                # 계산 값은 stack 안에 push()
        elif temp[i] == '*':                  # '*' 연산자 일 경우도 위에 elif 조건문과 똑같이 대응
            b = stack.pop()
            a = stack.pop()
            calc = a * b
            stack.append(calc)
    # print(stack)
    ans = stack[-1]                     # 마지막에 스택안에 남은 값이 총 계산 값 이므로 정답
    print(ans)





