import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()

    ans = 0
    for i in range(len(word)//2):
        if word[i] == word[len(word)-1-i]:
            ans = 1

    print('#{} {}'.format(tc, ans))