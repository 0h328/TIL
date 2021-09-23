import sys
sys.stdin = open('input.txt')
# from collections import defaultdict

def count_sub(node):
    cnt = 1
    for i in tree[node]:
        cnt += count_sub(i)
    return cnt

t = int(input())
for idx in range(1, t+1):
    e, n = map(int, input().split())
    tree = [[] for _ in range(e+2)]#defaultdict(list)
    info = list(map(int, input().split()))
    for i in range(e):
        tree[info[2*i]].append(info[2*i + 1])

    print('#{} {}'.format(idx, count_sub(n)))

