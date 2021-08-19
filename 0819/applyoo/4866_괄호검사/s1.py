import sys
sys.stdin = open('input.txt')


def palindrome():
    stack = []
    pair = {')': '(', '}': '{'}

    for i in sentence:
        if i in ('(', '{'):
            stack.append(i)
        elif i in (')', '}'):
            if len(stack) == 0 or pair[i] != stack.pop():
                return 0

    if stack:
        return 0
    return 1


T = int(input())

for test in range(T):
    sentence = input()
    print('#{} {}'.format(test+1, palindrome()))

