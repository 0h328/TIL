import sys
sys.stdin = open('input.txt')

def change_experession(original):
    stack = []
    priority = {'+': 0, '*': 1}
    result = ''

    for i in range(N):
        if original[i].isdigit():
            result += original[i]
        else:
            if not stack:
                stack.append(original[i])
            else:
                if priority[original[i]] > priority[stack[-1]]:     # >= 하면 정확한 후위표기식 X
                    stack.append(original[i])
                else:
                    while True:
                        result += stack.pop()
                        if not stack or priority[original[i]] > priority[stack[-1]]:
                            stack.append(original[i])
                            break
    if stack:
        while stack:
            result += stack.pop()

    return result

def calc_expression(expression):
    stack = []

    for i in range(len(expression)):
        if expression[i].isdigit():
            stack.append(expression[i])
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if expression[i] == '+':
                stack.append(num1 + num2)
            elif expression[i] == '*':
                stack.append(num1 * num2)

    return stack

T = 10

for tc in range(1, T+1):
    N = int(input())
    original = input()
    changed = change_experession(original)
    ans = calc_expression(changed)

    print('#{} {}'.format(tc, *ans))