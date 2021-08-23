import sys
sys.stdin = open('input.txt')

priority = {'*': 1, '+': 0}
stack = []
for idx in range(1, 11):
    length = int(input())
    s = input()
    new_s = ''
    top = -1
    for i in s:
        if i in '+*':
            while stack and priority[stack[top]] >= priority[i]:
                new_s += stack.pop()
                top -= 1
            stack.append(i)
            top += 1
        else:
            new_s += i
    while stack:
        new_s += stack.pop()
    # print(new_s)

    # 후위표현식 -> 계산
    for i in new_s:
        if i not in '+*':
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '*':
                stack.append(int(b)*int(a))
            else:  # i == '+'
                stack.append(int(b)+int(a))
    print('#{} {}'.format(idx, stack.pop()))