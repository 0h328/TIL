import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    condition = list(input().split())
    len_words = int(condition[1])
    words = list(input().split())
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt = [0 for _ in range(10)]
    result = [0 for _ in range(len_words)]

    for i in range(len_words):
        for j in range(10):
            if words[i] == num[j]:
                cnt[j] += 1

    for i in range(1, 10):
        cnt[i] += cnt[i - 1]

    for i in range(len_words):
        for j in range(10):
            if words[i] == num[j]:
                cnt[j] -= 1
                result[cnt[j]] = words[i]

    print(condition[0])
    print(*result, sep=' ')