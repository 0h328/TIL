import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s = list(input())
    stack = list()
    for i in range(len(s)):
        if len(stack) == 0 or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))

