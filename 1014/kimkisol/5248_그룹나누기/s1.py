import sys

sys.stdin = open('input.txt')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 출석번호마지막, M: 신청서 개수
    p = [0] + [x for x in range(1, N + 1)]
    m = list(map(int, input().split()))

    for i in range(M):
        union(m[i * 2], m[i * 2 + 1])

    set_p = set()
    for i in range(N + 1):
        set_p.add(find_set(i))

    print('#{} {}'.format(t, len(set_p) - 1))
