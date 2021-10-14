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


ans = []
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    p = [-1] * (N+1)
    for i in range(M):
        union(A[i*2], A[i*2+1])
    ans.append('#{} {}'.format(tc, len([i for i in p[1:] if i < 0])))
print(*ans, sep='\n')
