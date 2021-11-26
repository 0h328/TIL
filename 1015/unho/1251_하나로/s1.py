import sys
import heapq
sys.stdin = open('input.txt')


def prim():
    global ans

    heap = [(0, (x_li[0], y_li[0]))]

    while heap:
        w, coor = heapq.heappop(heap)
        if not visited.get((coor[0], coor[1])):
            visited[(coor[0], coor[1])] = 1
            ans += w
            for dis, co in linked[(coor[0], coor[1])]:
                if not visited.get((co[0], co[1])):
                    heapq.heappush(heap, (dis, co))


T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    x_li = list(map(int, input().split()))
    y_li = list(map(int, input().split()))
    E = float(input())

    ans = 0
    visited = {}
    linked = {}
    for i in range(N):
        linked[(x_li[i], y_li[i])] = []
        for j in range(N):
            if i != j:
                dis = (((x_li[i] - x_li[j])**2 + (y_li[i] - y_li[j])**2)**0.5)**2
                linked[(x_li[i], y_li[i])].append((dis, (x_li[j], y_li[j])))
    
    prim()

    answer.append('#{} {}'.format(tc, round(ans*E)))
print(*answer, sep='\n')