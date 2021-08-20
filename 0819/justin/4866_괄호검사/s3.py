def solve(code, is_pair):
    stack = []
    for i in range(len(code)):
        if code[i] == '{' or code[i] == '(':
            stack.append(code[i])
        elif code[i] == '}' or code[i] == ')':
            if not len(stack):
                is_pair = 0
                break
            else:
                tmp = stack.pop()
            if code[i] == ')':
                if tmp != '(':
                    is_pair = 0
                    break
            elif code[i] == '}':
                if tmp != '{':
                    is_pair = 0
                    break
    if len(stack) != 0:
        is_pair = 0
        return is_pair
    return is_pair


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    code = input()
    is_pair = 1
    ans = solve(code, is_pair)
    print('#{} {}'.format(tc, ans))