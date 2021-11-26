import sys
sys.stdin = open('input.txt')

# thought process: 5분 37초
# 먼저 후위 표기식으로 바꾸고
# 계산
# 연산자는 +, * 뿐
# 여는 괄호가 스택 안에 있고, 닫는 괄호를 만나면,
# 다시 여는 괄호를 만날때 까지 스택 요소들 pop

# 소요시간 약 28분
# 디버깅 약 20분
for tc in range(1, 11):     # 10 개의 테스트 케이스

    N = int(input())
    arr = input()
    stack = []
    temp = []

    # 후위 표기식으로 변환
    for i in range(N):

        if arr[i].isnumeric():              # i 위치 문자가 피연산자일 때
            temp.append(arr[i])             # temp 에 push
        elif arr[i] == '(':                 # i 위치 문자가 여는 괄호면 무조건 스택에 push
            stack.append(arr[i])
        elif arr[i] == ')':                     # i 위치 문자가 닫는 괄호면
            while stack[-1] != '(':             # 스택의 top 에 '(' 가 올 때까지
                temp.append(stack.pop())        # 스택 안의 연산자 pop, 것들을 temp 에 push
            stack.pop()                         # 여는 괄호는 제거 (사용 했으니)

        else:                               # i 위치의 문자가 연산자일 때
            if len(stack) == 0:             # 빈 스택인 경우
                stack.append(arr[i])        # 무조건 연산자 push
            else:                           # 스택안에 요소가 있을때
                while stack and stack[-1] != '(' and ord(arr[i]) >= ord(stack[-1]):     # i 위치의 요소보다 우선순위가 낮은 top 연산자를 만나거나 스택이 비어질때까지 스택 요스들을 pop 하고 temp 에 push
                    temp.append(stack.pop())
                stack.append(arr[i])        # i 위치 연산자는 스택에 push

    if len(stack) != 0:                     # 스택안에 연산자가 남아있으면,
        while len(stack) != 0:              # 모조리 temp 에 push
            temp.append(stack.pop())


    # 계산
    n = len(temp)

    for i in range(n):
        if temp[i].isnumeric():         # i 위치의 temp 가 피연산자일때
            stack.append(int(temp[i]))  # 무조건 스택에 push

        else:                           # i 위치의 temp 가 연산자일때
            b = stack.pop()
            a = stack.pop()
            if temp[i] == '+':          # '+' 연산자일 경우
                calc = a + b            # 스택 두개 값을 더하고
                stack.append(calc)      # 계산 값을 push
            elif temp[i] == '*':        # '*' 연산자일 경우
                calc = a * b
                stack.append(calc)
    print('#{} {}'.format(tc, stack[-1]))
