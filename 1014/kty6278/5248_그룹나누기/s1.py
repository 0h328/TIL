import sys
sys.stdin = open('input.txt')

def union(x, y):
    tree[find_set(y)] = find_set(x)

def find_set(x):
    while x != tree[x]:
        x = tree[x]
    return x

def make_set(x):
    tree[x] = x

for tc in range(int(input())):
    n, m = map(int, input().split())
    person = list(map(int, input().split()))
    tree = [0] * (n + 1)
    for i in range(n+1):
        make_set(i)
    for i in range(0, len(person), 2):
        union(person[i], person[i+1])
    cnt = set()
    for i in range(1, len(tree)):
        cnt.add(find_set(tree[i]))
    print('#{} {}'.format(tc+1, len(cnt)))