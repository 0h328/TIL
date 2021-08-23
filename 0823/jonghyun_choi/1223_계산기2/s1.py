import sys
sys.stdin = open('input.txt')

for case in range(10):
    N = int(input())
    data = input()
    ans = ''
    stack = []
    for char in data:
        if char == '*':
            while stack and stack[-1] == '*':
                ans += stack.pop()
            stack.append(char)
        elif char == '+':
            while stack and stack[-1] != '+':
                ans += stack.pop()
            stack.append(char)
        else:
            ans += char
    while stack:
        ans += stack.pop()

    res = 0
    for i in ans:
        if i.isdecimal():
            stack.append(i)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a)*int(b))
        elif i == '+':
            c = stack.pop()
            d = stack.pop()
            stack.append(int(c)+int(d))
    print('#{} {}'.format(case + 1,''.join(map(str,stack))))

