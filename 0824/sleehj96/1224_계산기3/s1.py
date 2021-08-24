import sys
sys.stdin = open('input.txt')


T = 10
tc = 1
while tc <= T:
    N = int(input())
    data = input()
    stack = []
    string = ''

    # infix to postfix
    for letter in data:
        if letter == '(':           # 1. 열린 괄호면
            stack.append(letter)    # 스택에 push

        elif letter.isnumeric():    # 2. 숫자면
            string += letter        # 프린트할 문자열에 추가

        else:                       # 3. 다른 연산자면
            if '(' in stack:            # 1> ( 가 있으면
                if letter == '*':           # 1) * 일 때
                    while stack[-1] != '(' and stack[-1] == '*':
                        string += stack.pop()
                    stack.append(letter)

                elif letter == '+':         # 2) + 일 때
                    while stack[-1] != '(':
                        string += stack.pop()
                    stack.append(letter)

                elif letter == ')':         # 3) ) 일 때
                    while stack[-1] != '(':
                        string += stack.pop()
                    stack.pop()

            else:                       # 2> ( 가 없으면

                if letter == '*':           # 1) * 일 때
                    while stack and stack[-1] == '*':
                        string += stack.pop()
                    stack.append(letter)

                elif letter == '+':         # 2) + 일 때
                    while stack:
                        string += stack.pop()
                    stack.append(letter)

    while stack:                # 스택 남아 있으면
        string += stack.pop()

    # read postfix notation
    for char in string:
        if char.isnumeric():
            stack.append(int(char))

        else:
            n2 = stack.pop()
            n1 = stack.pop()

            if char == '*':
                stack.append(n1*n2)
            elif char == '+':
                stack.append(n1+n2)

    ans = stack.pop()

    print('#{0} {1}'.format(tc, ans))
    # break
    tc += 1

