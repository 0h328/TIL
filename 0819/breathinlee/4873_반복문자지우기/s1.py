import sys
sys.stdin = open("input.txt")

def repeated_word(words):
    stack = []
    stack.append(words[0])
    for i in range(1, len(words)):
        if len(stack) == 0:
            stack.append(words[i])
        else:
            if stack[-1] == words[i]:
                stack.pop()
            else:
                stack.append(words[i])

    if stack:
        return len(stack)
    return 0


T = int(input())
for tc in range(1, T+1):
    words = input()
    print('#{} {}'.format(tc, repeated_word(words)))