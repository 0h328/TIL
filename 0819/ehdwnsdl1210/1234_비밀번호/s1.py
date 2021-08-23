import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, word = map(int, input().split())
    stack = []

    stack.append(word)

    for i in range(1, N):
        if len(stack) == 0 or stack[-1] != stack[i]:
            stack.append(stack[i])
        else:
            stack.pop()

    print('#{} {}'.format(tc, len(stack)))