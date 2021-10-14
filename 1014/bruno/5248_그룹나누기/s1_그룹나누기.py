import sys
sys.stdin = open('input.txt')


def make_set(x):
    p[x] = x


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    x_list = list(map(int, input().split()))
    p = [0] * (N + 1)
    for i in range(N + 1):
        make_set(i)
    for i in range(M):
        union(x_list[i * 2], x_list[i * 2 + 1])

    result = []
    for i in range(len(p)):
        result.append(find_set(i))

    print('#{} {}'.format(tc, len(set(result)) - 1))