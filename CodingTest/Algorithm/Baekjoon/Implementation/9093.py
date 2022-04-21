import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    sentence = list(input().split())

    for word in sentence:
        print(word[::-1], end=' ')
    print()

