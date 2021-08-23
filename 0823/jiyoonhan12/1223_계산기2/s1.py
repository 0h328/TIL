import sys
sys.stdin = open('input.txt')

def solve():
    stack = []
    data_num = ''
    for char in data:
        if char == '*':
            stack.append(char)
        elif char == '+':
            if stack and stack[len(stack)-2] == '*':
                while stack:
                    data_num += stack.pop()
            stack.append(char)
            data_num += stack.pop()
        else:
            data_num += char
    while stack: # 스택에 남은 * 처리
        data_num += stack.pop()

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
    return result[0] + result[1]


for t in range(1, 11):
    N = int(input())
    data = input() # 중위 표기식
    print('#{} {}'.format(t, solve()))