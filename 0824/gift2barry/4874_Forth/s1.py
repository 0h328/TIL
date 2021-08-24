import sys
sys.stdin = open('input.txt')

# thought process: 1분 30초
# 숫자는 스택에 넣는다.
# 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
# ‘.’은 스택에서 숫자를 꺼내 출력한다.
# 연산 불가능 한 경우 error 출력

# 소요시간 18분, 9 / 10 tc 통과
# 디버깅 6분 18초
for tc in range(1, int(input())+1):

    arr = list(map(str, input().split()))
    N = len(arr)
    stack = []

    for i in range(N):
        if arr[i].isnumeric():                  # 피연산자이면
            stack.append(int(arr[i]))           # push

        elif arr[i] == '.':                         # '.' 문자 만나면,
            if len(stack) == 1:                     # 스택이 하나만 남았으면
                print('#{} {}'.format(tc, stack[-1]))   # 정답 반환
            else:                                   # 스택이 1개가 아니면
                print('#{} error'.format(tc))       # 에러 반환
                break                               # 루프 종료

        else:                                   # 연산자일때,
            if len(stack) < 2:                  # 스택 안에 피연산자가 충분하지 않을경우 계산을 못하니까
                print('#{} error'.format(tc))   # 에러 반환
                break                           # 루프 종료
            else:                       # 스택 안에 피연산자가 충분할 경우
                b = stack.pop()         # pop 할 두개의 값을 변수에 할당
                a = stack.pop()
                if arr[i] == '+':       # + 연산자일 경우
                    calc = a + b        # 스택 두개 값을 더하고
                    stack.append(calc)  # 계산 값을 push
                elif arr[i] == '*':     # * 연산자일 경우
                    calc = a * b
                    stack.append(calc)
                elif arr[i] == '-':     # - 연산자일 경우
                    calc = a - b
                    stack.append(calc)
                elif arr[i] == '/':     # / 연산자일 경우
                    calc = a // b
                    stack.append(calc)