import sys
sys.stdin = open('input.txt')

def solve():
    # for char in line:
    #     if char == '(' or char == '{':
    #         stack.append(char)
    #     elif char == ')' or char == '}':
    #         if stack:
    #             popped = stack.pop()
    #         else:
    #             return 0
    #         if popped == '{' and char == ')':
    #             return 0
    #         if popped == '(' and char == '}':
    #             return 0
    # if stack:
    #     return 0
    # else:
    #     return 1

    bracket = {'(': ')', '{': '}'}
    for char in line:
        if char in bracket.keys():
            stack.append(char)
        elif char in bracket.values():
            if stack and char == bracket[stack[-1]]:
                stack.pop()
            else:
                return 0
        else:
            continue
    if stack:
        return 0
    else:
        return 1


T = int(input())
for t in range(1, T+1):
    line = input()
    stack = []
    print('#{} {}'.format(t, solve()))