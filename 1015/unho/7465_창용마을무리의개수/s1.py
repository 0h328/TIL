import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def union(a, b):
    s[find_set(b)] = find_set(a)


T = int(input())
answer = []

for tc in range(1, T+1):
    N, M = map(int, input().split())
    s = [i for i in range(N+1)]

    for _ in range(M):
        p1, p2 = map(int, input().split())
        union(p1, p2)

    for i in range(N+1):
        find_set(i)
    
    answer.append('#{} {}'.format(tc, len(set(s))-1))
print(*answer, sep='\n')