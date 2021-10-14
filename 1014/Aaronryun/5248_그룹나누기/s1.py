import sys

sys.stdin = open('input.txt')

def find_set(x):
    if x == parent[x]:
        return x
    return find_set(parent[x])

def union(x, y):
    parent[find_set(y)] = find_set(x)


for test in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    parent = [i for i in range(N + 1)]

    for i in range(0, M * 2, 2):
        union(data[i], data[i + 1])
    # print(parent)
    result = set()
    for j in range(1, N + 1):
        result.add(find_set(j))
    # print(result)
    print('#{} {}'.format(test, len(result)))
