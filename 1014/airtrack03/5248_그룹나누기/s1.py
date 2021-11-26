import sys

sys.stdin = open('input.txt')

T = int(input())

def make_set(num):
    p[num] = num


def find_set(num):
    while p[num] != num:
        num = p[num]
    return num


def union(node1, node2):
    p[find_set(node2)] = find_set(node1)


for tc in range(1, T+1):
    N, M = map(int, input().split())

    p = [0] * (N+1)

    for i in range(1, N+1):
        make_set(i)

    data = list(map(int, input().split()))
    for i in range(M):
        v1, v2 = data[i*2], data[i*2 + 1]
        union(v1, v2)

    for i in range(1, N+1):
        p[i] = find_set(p[i])

    ans = len(set(p[1:]))

    print('#{} {}'.format(tc, ans))