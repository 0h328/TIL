import sys
import heapq
sys.stdin = open('input.txt')

# prim default / prim heapq / kruskal

# prim heapq
def prim():
    global ans
    heap = [(0, 0)]
    
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = 1
            for weight, node in linked[v]:
                if not visited[node]:
                    heapq.heappush(heap, (weight, node))
    return ans

T = int(input())
answer = []

for tc in range(1, T+1):
    V, E = map(int, input().split())
    linked = {}                         # link relations
    ans = 0                             # accumulatesum
    visited = [0] * (V+1)               # visited node

    for _ in range(E):                      
        n1, n2, w = map(int, input().split())
        linked[n1] = linked.get(n1, []) + [(w, n2)]
        linked[n2] = linked.get(n2, []) + [(w, n1)]

    answer.append('#{} {}'.format(tc, prim()))

print(*answer, sep='\n')


# prim default
""" 
def prim():
    for _ in range(V):
        min_idx = -1
        min_value = 1e10

        for i in range(V+1):
            if not visited[i] and sel_weight[i] < min_value:
                min_idx = i
                min_value = sel_weight[i]
        visited[min_idx] = 1

        for i in linked[min_idx]:
            if not visited[i[0]] and i[1] < sel_weight[i[0]]:
                sel_weight[i[0]] = i[1]

    return sum(sel_weight)

T = int(input())
answer = []

for tc in range(1, T+1):
    V, E = map(int, input().split())
    linked = {}                     # link relations
    sel_weight = [1e10] * (V+1)
    sel_weight[0] = 0               # start weight is 0 (start node - 0)     
    visited = [0] * (V+1)           # visited node

    for _ in range(E):              # none direction
        n1, n2, w = map(int, input().split())
        linked[n1] = linked.get(n1, []) + [(n2, w)]
        linked[n2] = linked.get(n2, []) + [(n1, w)]
        
    answer.append('#{} {}'.format(tc, prim()))

print(*answer, sep='\n')
"""