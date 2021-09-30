import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()

    n, m = len(t), len(p)

    res = []
    for j in range(m):
        cnt = 0
        for i in range(n):
            if p[j] == t[i]:
                cnt += 1
                res.append(cnt)

    print('#{} {}'.format(tc, max(res)))