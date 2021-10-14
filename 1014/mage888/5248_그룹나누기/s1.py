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
    data = list(map(int, input().split()))
    p = [0] * (N+1)

    for i in range(N+1):
        p[i] = i

    for i in range(M):
        union(data[2*i], data[2*i+1])

    tmp = set()
    for i in range(N+1):
        tmp.add(find_set(p[i]))

    print('#{} {}'.format(tc, len(tmp)-1))

