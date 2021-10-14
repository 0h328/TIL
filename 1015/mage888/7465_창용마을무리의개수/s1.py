import sys
sys.stdin = open('input.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [0] * (N+1)
    for i in range(N+1):
        p[i] = i

    for _ in range(M):
        try:
            h1, h2 = map(int, input().split())
            union(h1, h2)
        except:
            pass

    res = set()
    for i in range(N+1):
        res.add(find_set(p[i]))

    print('#{} {}'.format(tc, len(res)-1))