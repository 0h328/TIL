import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    T = int(input())
    data = input()
    stack = []
    stack_num = []

# isp = {')' : -, '*, /' : 2, '+, -' : 1, '(' : 0}
# icp = {')' : -, '*, /' : 2, '+, -' : 1, '(' : 3}

    # 중위 표현식 -> 후위 표현식
    for char in data:
        if char == '*':                                # * 연산자의 경우 stack에 push
            stack.append(char)
        elif char == '+':                              # + 연산자의 경우
            if len(stack) == 0:                        # stack이 비어있으면 push
                stack.append(char)
            else:
                while stack:                           # stack이 비어있지 않은 경우
                    stack_num.append(stack.pop())      # stack top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 pop
                stack.append(char)                     # 그 후 토큰의 연산자 push
        else:                                          # 피연산자의 경우 stack_num에 push
            stack_num.append(char)

    while stack:                                       # stack에 남아 있는 연산자를 모두 pop하여 push
        stack_num.append(stack.pop())
    # print(stack_num)

    # 후위 표현식 -> 계산
    cal = []
    for char in stack_num:
        if char == '*' or char == '+':                 # 연산자의 경우 피연산자를 두번 pop()하여 연산
            a = cal.pop()
            b = cal.pop()
            if char == '*':
                cal.append(int(b) * int(a))            # 연산 결과를 다시 cal에 push
            else:
                cal.append(int(b) + int(a))            # 연산 결과를 다시 cal에 push
        else:
            cal.append(char)                           # 피연산자의 경우 cal에 push
    # print(cal)
    print('#{} {}'.format(tc, *cal))
