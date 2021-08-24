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

    for char in data:

        if char == '*':
            stack.append(char)

        elif char == '+':
            if not stack:
                stack.append(char)
            else:
                # print(stack)
                while stack[-1] == '*':
                    string += stack.pop()
                    if not stack:
                        break

                stack.append(char)

        else:
            string += char
    # print(stack)
    while stack:
        string += stack.pop()

    # print(string)

    # 2. 후위 표기법 읽어오기
    stack2 = []
    for idx in range(len(string)):

        if string[idx].isnumeric():
            stack2.append(int(string[idx]))

        else:
            n1 = stack2.pop()
            n2 = stack2.pop()

            if string[idx] == '*':
                stack2.append(n1*n2)
            elif string[idx] == '+':
                stack2.append(n1+n2)

    # print(stack2)
    ans = stack2.pop()
    print('#{0} {1}'.format(tc, ans))
    # break
    tc += 1
