import sys
sys.stdin = open('input.txt')

#은승원님 풀이 참고
for t in range(1, 11):
    N = int(input())
    formula = input()
    stack = []
    postfix = ''
    isp = {'*': 2, '/': 2, '+': 1, '-': 1}

    for char in formula:
        if char.isdigit():
            postfix += char
        else:
            if char == ')':
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            elif char == '(':
                stack.append(char)
            else:
                while stack and isp.get(char, 0) <= isp.get(stack[-1], 0):
                    postfix += stack.pop()
                stack.append(char)
    while stack:
        postfix += stack.pop()

    ans = []
    for char in postfix:
        if char.isdigit():
            ans.append(int(char))
        else:
            num2 = ans.pop()
            num1 = ans.pop()
            if char == '*':
                ans.append(num1 * num2)
            elif char == '/':
                ans.append(num1 // num2)
            elif char == '+':
                ans.append(num1 + num2)
            elif char == '-':
                ans.append(num1 - num2)
    print('#{} {}'.format(t, ans[0]))
