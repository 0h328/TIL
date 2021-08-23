import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []

    stack.append(word[0])

    for i in range(1, len(word)):
        if len(stack) == 0 or stack[-1] != word[i]:
            stack.append(word[i])
        else:
            stack.pop()

    print('#{} {}'.format(tc, len(stack)))