import sys
sys.stdin = open('input.txt')

num = int(input())
for T in range(1, num+1):
    word = input()
    sentence = input()

    if word in sentence:
        result = 1
    else:
        result = 0

    print('#{0} {1}'.format(T, result))