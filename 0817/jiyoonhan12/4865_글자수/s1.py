import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    str1 = list(set(input()))
    str2 = input()

    cnt = [0] * len(str1)
    for char in str2:
        if char in str1:
            cnt[str1.index(char)] += 1

    res = max(cnt)

    print('#{} {}'.format(t, res))