import sys
sys.stdin = open('input.txt')


def solve():
    stack = []
    data_num = ''

    for char in data:
        if char == '*':
            stack.append(char)
        elif char == '+':
            while stack and stack[-1] != '(':
                data_num += stack.pop()
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                data_num += stack.pop()
            stack.pop()
        else:
            data_num += char

    #print(data_num)

    result = []
    for c in data_num:
        if c == '*':
            right = result.pop()
            left = result.pop()
            result.append(left * right)
        elif c == '+':
            if len(result) > 1:
                right = result.pop()
                left = result.pop()
                result.append(left + right)
        else:
            result.append(int(c))
    return result[0]

for t in range(1, 11):
    num = int(input()) # not used
    data = input()
    print('#{} {}'.format(t, solve()))