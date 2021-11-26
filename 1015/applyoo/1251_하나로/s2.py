import sys
sys.stdin=open('input.txt')

def cost(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2) * E


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
    N = int(input())
    X, Y = list(map(int, input().split())), list(map(int, input().split()))
    E = float(input())

    p = [-1] * (N+1)
    grp = []
    for i in range(N):
        for j in range(i+1, N):
            grp.append((i, j, cost(X[i], Y[i], X[j], Y[j])))

    grp.sort(key=lambda x: x[2])

    res = cnt = 0
    for a, b, c in grp:
        if union(a, b):
            cnt += 1
            res += c
            if cnt == N - 1: break

    ans.append('#{0} {1:.0f}'.format(tc, res))

print(*ans, sep='\n')
