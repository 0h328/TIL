import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    stack = []  # 처음 표기법 변환할때 연산자를 저장하기 위한 stack
    result = [] # 처음 후위 표기법으로 변환하였을 때를 저장하기 위한 list
    arr = []    # 후위표기법으로 계산된 식을 계산하기위해 저장하는 stack
    num = list(input())
    for i in range(N):  # step1 중위 표기법을 후위 표기법으로 표현
        if num[i] == '+' and stack: # 우선순위가 낮은 +를 받으면 그 +를 제외한 나머지 stack을 모두 pop하고 연산자는 push
            while stack:
                result.append(stack.pop())
            stack.append(num[i])
        elif num[i] == '+' or num[i] == '*':    # stack이 비어있거나 *를 연산자로 받은경우 우선순위가 높아 push
            stack.append(num[i])
        else:
            result.append(num[i])   # 나머지 피연산자는 모두 push
    while stack:
        result.append(stack.pop())  # stack이 빌때 까지 pop
    print(result)

    for i in range(N):  # step 2 후위표기법을 통하여 계산하는 과정
        if result[i] == '+':    # 각각 연산자에 따라 저장된 stack에서 피연산자를 2개씩 꺼내어 계산
            arr.append(arr.pop() + arr.pop())
        elif result[i] == '*':
            arr.append(arr.pop() * arr.pop())
        else:   # 피연산자는 stack에 저장
            arr.append(int(result[i]))
    while arr:  # 모든 계산이 끝난 경우 저장된 arr stack의 결과값 출력.
        print('#{} {}'.format(tc, arr.pop()))

