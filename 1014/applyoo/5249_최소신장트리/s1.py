import sys
sys.stdin=open('input.txt')


def find(x):
    if p[x] < 0: return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    x, y = find(x), find(y)

    if x != y:
        if p[x] <= p[y]:
            p[x] += p[y]
            p[y] = x
        else:
            p[y] += p[x]
            p[x] = y
        return True
    return False


ans = []
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]

    p = [-1] * (N+1)
    A.sort(key=lambda x: x[2])

    res = cnt = 0
    for n1, n2, w in A:
        if union(n1, n2):
            res += w
            cnt +=1
            if cnt == N: break

    ans.append('#{} {}'.format(tc, res))
print(*ans, sep='\n')
