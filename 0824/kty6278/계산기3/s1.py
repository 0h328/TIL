import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    data = input()
    stack = []
    num = '' # 후위 표현식 저장 공간
    dic = {'(' : 0 ,'*' : 2 ,'+' : 1, ')' : 0}
    #1. 중위 표현식 -> 후위 표현식
    for char in data:
        if char.isdigit(): # 숫자인 경우 출력
            num += char
        elif char == '(':    # 열린 괄호인 경우 stack 추가
            stack.append(char)
        elif char == ')':    # 닫힌 괄호인 경우
            while stack and stack[-1] != '(':   # stack에 한개라도 존재하고 top이 (일 때까지
                num += stack.pop()              # 열린괄호가 나오기 전까지 pop 출력
            stack.pop()                         # 마지막으로 남아있는 열린괄호 제거
        else:    # 연산자인경우
            while stack and dic[stack[-1]] >= dic[char]: # stack에 한개라도 존재하고 우선순위 고려
                num += stack.pop()
            stack.append(char)
    while stack:
        num += stack.pop()
    result = []
    for n in num:
        # print(type(n))
        if n == '*':
            a = result.pop()
            b = result.pop()
            c = b * a
            result.append(c)
        elif n == '+':
            a = result.pop()
            b = result.pop()
            c = b + a
            result.append(c)
        else:
            result.append(int(n))
    print('#{} {}'.format(tc+1, *result))
