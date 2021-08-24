import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    my_list = list(input())
    stack = []
    my_str = ''

    isp = {
        '*': 2,
        '+': 1,
        '(': 0,
    }

    for char in my_list:
        if char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                my_str += stack.pop()
            stack.pop()
        elif char == '*' or char == '+':
            while stack and isp.get(stack[-1]) >= isp.get(char):
                my_str += stack.pop()
            stack.append(char)
        else:
            my_str += char

    while stack:
        my_str += stack.pop()

    # print(my_str)

    stack = []

    for char in my_str:
        if char.isnumeric():
            stack.append(int(char))
        elif char == '*':
            stack.append(stack.pop(-2) * stack.pop(-1))
        elif char == '+':
            stack.append(stack.pop(-2) + stack.pop(-1))

    print('#{} {}'.format(tc,stack[0]))