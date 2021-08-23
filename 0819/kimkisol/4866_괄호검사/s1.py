import sys
sys.stdin = open('input.txt')

def Is_Parenthesis(chars):
    stack = []
    for i in range(len(chars)):
        if chars[i] == '(':
            stack.append('(')
        elif chars[i] == '{':
            stack.append('{')
        elif chars[i] == ')':
            if len(stack) == 0 or stack.pop() != '(': #없으면 런타임에러
                return 0
        elif chars[i] == '}':
            if len(stack) == 0 or stack.pop() != '{':  # 없으면 런타임에러
                return 0
    if stack:
        return 0
    return 1

T = int(input())

for t in range(1, T+1):
    chars = input()
    print('#{} {}'.format(t, Is_Parenthesis(chars)))
