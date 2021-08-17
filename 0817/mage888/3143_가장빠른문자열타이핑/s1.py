import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    t, p = input().split()
    n, m = len(t), len(p)

    cnt = 0
    i = 0
    while i < n-m+1:
        for j in range(m):
            if p[j] != t[i+j]:
                break
        else:
            cnt += 1
            i = i + m - 1
        i += 1

    print(n - (cnt * m) + cnt)