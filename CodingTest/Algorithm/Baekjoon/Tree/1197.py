import sys
input = sys.stdin.readline

V, E = map(int, input().split())
p = [i for i in range(V + 1)]
edge = sorted((list(map(int, input().split())) for _ in range(E)), key=lambda x: x[2])

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

ans = 0
for s, e, w in edge:
    start = find_set(s)
    end = find_set(e)
    if start != end:
        if start > end:
            p[start] = end
        else:
            p[end] = start
        ans += w

print(ans)