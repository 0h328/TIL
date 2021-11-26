import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def find_word(t, p):

    i = 0
    j = 0
    cnt = 0

    while i < n and j < m:
        if t[i] == p[j]:
            i += 1
            j += 1
        i += 1
        j = 0
        if j == m:
            cnt += 1

    return cnt

    print('#{} {}'.format(tc, find_word(t, p)))

for _ in range(10):
    tc = int(input())
    p = input()
    t = input()

    n, m = len(t), len(p)

