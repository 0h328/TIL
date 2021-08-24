import sys
sys.stdin = open('input.txt')

N = int(input())  # 테스트 케이스 갯수
for tc in range(1, N + 1):                          # N개의 테스트 케이스
    data = map(str, input().split()) # 중위 표기식   # 후위 표기식
    stack = []                                      # 스택
    num = ""                                        # 결과

    #2. 후위 표현식 -> 계산
    try:
        for char in data:                               # num의 글자를 하나씩 빼서

            if char == "." and len(stack) > 1:          # 중간에 . 나오는 경우
                num = "error"
                break

            elif char == ".":                           # 끝에 . 나오는 경우
                num = stack.pop()                           # num에는 최종 결과값 출력
                break

            elif ('0' <= char) and (char <= '9'):
                stack.append(char)                  # stack에 바로 추가

            else:
                if char == "*":                         # 해당 문자가 * 이면
                    a = stack.pop()                     # a에 pop
                    b = stack.pop()                     # b에 pop
                    stack.append(int(b) * int(a))       # stack에 b * a 결과를 추가
                elif char == "/":
                    a = stack.pop()                     # a에 pop
                    b = stack.pop()                     # b에 pop
                    stack.append(int(b) // int(a))       # stack에 b // a 결과를 추가
                elif char == "+":                       # 해당 문자가 + 이면
                    a = stack.pop()                     # a에 pop
                    b = stack.pop()                     # b에 pop
                    stack.append(int(b) + int(a))       # stack에 b + a 결과를 추가
                elif char == "-":                       # 해당 문자가 + 이면
                    a = stack.pop()                     # a에 pop
                    b = stack.pop()                     # b에 pop
                    stack.append(int(b) - int(a))       # stack에 b + a 결과를 추가


    except IndexError:
        num = "error"

    finally:
        print("#{} {}".format(tc, num))                 # print