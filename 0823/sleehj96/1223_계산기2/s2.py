import sys
sys.stdin = open('input.txt')

T = 10
tc = 1
while tc <= T:
    str_len = int(input())
    data = input()

    # 1. 중위 표기법 -> 후위 표기법
    stack = []
    string = ''

    for char in data:   # data 하나씩 순회

        if char == '*':         # *는 최우선 순위
            stack.append(char)  # push

        elif char == '+':       # +는 눈치보면서 push

            if not stack:       # stack이 비어있으면
                stack.append(char)  # push

            else:               # 차 있으면
                while stack:    # 스택을 다 비울때 까지
                    string += stack.pop()   # pop
                # 단독 최우선순위일 경우에만 push가 가능한데
                # +든 *든 스택에 들어있으면 단독 최우선순위가 불가하기 때문

                stack.append(char)  # 그리고 push

        else:               # 숫자면
            string += char  # 그냥 string

    while stack:        # 스택을 비우는 작업 필요
        string += stack.pop()   # 순서대로 pop

    # 2. 후위 표기법 읽어오기
    # 돌다가 연산자를 만나면 앞의 두 숫자를 연산자로 연산
    stack2 = []
    for idx in range(len(string)):

        if string[idx].isnumeric():         # 숫자는
            stack2.append(int(string[idx]))  # 스택에 쌓음

        else:                   # 연산자는
            n1 = stack2.pop()   # 스택에서 두개를 뽑아
            n2 = stack2.pop()

            if string[idx] == '*':      # 연산
                stack2.append(n1*n2)
            elif string[idx] == '+':
                stack2.append(n1+n2)

    ans = stack2.pop()
    print('#{0} {1}'.format(tc, ans))
    tc += 1
