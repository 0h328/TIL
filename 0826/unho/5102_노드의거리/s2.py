'''
DFS 활용
visited 로 이동한 거리 구현
'''

import collections
import sys
sys.stdin = open('input.txt')



def dfs(start, end):
    q = collections.deque([start])

    while q:
        node = q.popleft()
        visited[node] += 1
        for e in linked[node]:
            if not visited[e]:
                q.append(e)
                visited[e] = visited[node]

        if node == end:
            return



test_case = int(input())

for tc in range(1, test_case+1):
    V, E = map(int, input().split())
    linked = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):                      # 노드간 연결 내용 초기화 / 인접리스트
        v1, v2 = map(int, input().split())
        linked[v1].append(v2)
        linked[v2].append(v1)

    start, end = map(int, input().split())  # 시작 / 끝 노드
    dfs(start, end)                # DFS 함수 호출

    if visited[end] == 0:
        visited[end] += 1

    print('#{} {}'.format(tc, visited[end]-1))