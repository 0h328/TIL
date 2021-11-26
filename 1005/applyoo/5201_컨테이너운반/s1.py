import sys
sys.stdin = open('input.txt')


ans = []
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)

    wi = ti = 0
    res = 0
    while wi < len(w) and ti < len(t):
        if t[ti] >= w[wi]:
            res += w[wi]
            wi += 1
            ti += 1
        else:
            wi += 1
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
