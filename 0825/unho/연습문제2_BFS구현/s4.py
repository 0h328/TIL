"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""
import sys
import queue
sys.stdin = open('input.txt')


def bfs(v):
    global distance

    q = queue.Queue()
    q.put(v)
    last = v

    while not q.empty():
        node = q.get()
        if not visited[node]:
            visited[node] = True
            if linked.get(node):
                for e in linked.get(node):
                    q.put(e)

        if node == last:
            distance += 1
            last = e


# V(ertex), E(dge)
v, e = map(int, input().split())

# 간선 정보 초기화
linked = {}

# Graph 초기화
in_list = list(map(int, input().split()))
for i in range(len(in_list)//2):
    linked[in_list[i*2]] = linked.get(in_list[i*2], []) + [in_list[i*2+1]]

# 방문 표시 초기화
visited = [False] * (v+1)

# bfs 탐색 시작
distance = 0
bfs(1)
print(distance)