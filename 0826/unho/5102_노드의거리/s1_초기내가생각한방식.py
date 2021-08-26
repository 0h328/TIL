'''
최소 이동을 구하므로 BFS 활용
7개만 맞음
'''

import collections
import sys
sys.stdin = open('input.txt')



def bfs(start, end):
    q = collections.deque()
    q.append(start)
    last = q[0]
    cnt = 1

    while q:
        node = q.popleft()


        if not visited[node]:
            visited[node] = True

            for e in linked[node]:
                if not visited[e]:
                    q.append(e)

                if e == end:
                    return cnt

        if q and last == node:
            cnt += 1
            last = q.pop()
            q.append(last)

    return 0

test_case = int(input())

for tc in range(1, test_case+1):
    V, E = map(int, input().split())
    visited = [False] * (V+1)
    linked = [[] for _ in range(V+1)]


    for _ in range(E):
        v1, v2 = map(int, input().split())
        linked[v1].append(v2)
        linked[v2].append(v1)

    # print(linked)

    start, end = map(int, input().split())
    answer = bfs(start, end)


    print('#{} {}'.format(tc, answer))