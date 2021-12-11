import sys
sys.setrecursionlimit(int(1e9))
# input = sys.stdin.readline
sys.stdin = open('input.txt')

def dfs(s):
    v[s] = 1
    for i in tree[s]:
        if not v[i]:
            p[i] = s
            dfs(i)

N = int(input())
tree = [[] for _ in range(N+1)]
v = [0] * (N+1)
p = [0] * (N+1)p
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
print(tree)

dfs(1)
for i in range(2, N+1):
    print(p[i])