import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):                         # 10개의 테스트 케이스
    N = input()                                 # 테스트 케이스 갯수
    data = input() # 중위 표기식                 # 테스트 케이스
    stack = []                                  # 스택
    num = ""                                    # 저장할 문자
    #1. 중위 표현식 -> 후위 표현식

    for char in data:                           # 테스트 케이스 하나씩 돌림
        if char == "(":                         # 해당 문자가 ( 이면
            stack.append(char)                  # stack 에 추가
        elif char == "*":                       # 해당 문자가 *이면
            while stack and stack[-1] == "*":   # stack이 비거나 top이 *이 아닐 때까지
                num += stack.pop()              # num에 stack값을 추가
            stack.append(char)                  # stack에 현재 문자추가
        elif char == "+":                       # 해당 문자가 + 이면
            # stack.append(char)
            # 이 경우 고려해야 할 사항?
            # stack이 비어있는지 여부 판단 & stack의 가장 위 (top)가 * 연산자인지 확인
            while stack and (stack[-1] == "*" or stack[-1] == "+"):    # stack이 비거나 top이 +가 아닐 때까지
                num += stack.pop()              # num에 stack값을 추가
            stack.append(char)                  # stack에 현재 문자 추가
        elif char == ")":                       # 해당 문자가 )이면
            while stack[-1] != "(":   # stack이 비거나 top이 (일 때 까지
                num += stack.pop()              # num에 stack값을 추가
            stack.pop()                         # ( 내보내기
        else:                                   # 숫자이면
            num += char                         # 바로 num에 추가
    while stack:                                # stack이 빌 때까지
        num += stack.pop()                      # num에 추가

    #2. 후위 표현식 -> 계산

    for char in num:                            # num의 글자를 하나씩 빼서
        if char == "*":                         # 해당 문자가 * 이면
            a = stack.pop()                     # a에 pop
            b = stack.pop()                     # b에 pop
            stack.append(int(b) * int(a))       # stack에 b * a 결과를 추가
        elif char == "+":                       # 해당 문자가 + 이면
            a = stack.pop()                     # a에 pop
            b = stack.pop()                     # b에 pop
            stack.append(int(b) + int(a))       # stack에 b + a 결과를 추가
        else:                                   # 숫자이면
            stack.append(char)                  # stack에 바로 추가
    num = stack.pop()                           # num에는 최종 결과값 출력
    print("#{} {}".format(tc, num))             # print