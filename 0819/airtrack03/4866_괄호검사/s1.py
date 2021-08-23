import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()
    stack = []
    brackets = ['(', ')', '{', '}']
    ans = 1

    for char in data:
        if char not in brackets:
            continue

        if char == brackets[0] or char == brackets[2]:
            stack.append(char)
        elif char == brackets[1]:
            # 비어있는 스택에 닫는 괄호 들어가면 ans 0으로 바꿔줘야 하므로 append하면서 break
            if not stack:
                stack.append(char)
                break
            # 짝 맞으면 break
            elif stack[-1] == brackets[0]:
                stack.pop()
            # 마지막 여는 괄호랑 짝 안 맞으면 ans = 0
            else:
                break
        else:
            if not stack:
                stack.append(char)
                break
            elif stack[-1] == brackets[2]:
                stack.pop()
            else:
                break

    if stack:
        ans = 0

    print('#{} {}'.format(tc, ans))