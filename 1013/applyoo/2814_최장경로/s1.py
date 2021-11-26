import sys
sys.stdin=open('input.txt')


from collections import defaultdict


def dfs(n, v):
    global res, x
    for i in grp[n]:
        if i not in v:
            v.add(i)
            dfs(i, v)  # 백트래킹
            v.remove(i)

    if res < len(v):  # 길이가 더 긴 경우
        res = len(v)  # 갱신
        x = n  # 노드도 갱신


ans = []
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    grp = defaultdict(set)
    for _ in range(M):
        x, y = map(int, input().split())
        grp[x].add(y)
        grp[y].add(x)

    res, x = 0, 1  # 최장 길이, 마지막 인덱스
    dfs(1, set([1]))  # 1에서 가장 먼 인덱스(x)를 얻음
    dfs(x, set([x]))  # x에서 가장 긴 경로(최장 길이)를 얻음

    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
