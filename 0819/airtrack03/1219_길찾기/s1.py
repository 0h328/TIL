import sys

sys.stdin = open('input.txt')

T = 10

def dfs(start, dest):
    if start == dest:   # 출발지와 목적지가 같아지면 찾은 것이므로 return True
        return True
    visited[start] = 1

    for nxt in graph[start]:
        if not visited[nxt]:
            if dfs(nxt, dest):  # 모든 길을 찾는 것이 아닌 도달 여부만 찾으므로 하나라도 찾으면 함수 종료
                return True

for _ in range(T):
    V = 100
    tc, E = map(int, input().split())
    A, B = 0, 99

    visited = [0 for _ in range(V)]
    graph = [[] for _ in range(V)]          # 인접 리스트 위한 graph

    temp = list(map(int, input().split()))  # 데이터 받아오기 위한 임시 변수

    for i in range(1, len(temp), 2):
        graph[temp[i-1]].append(temp[i])    # temp 통해 인접 리스트 채우기

    ans = 1 if dfs(A, B) else 0             # dfs(A, B)에서 True 반환하면 길 찾은 것으로 ans = 1, 반대는 ans = 0

    print('#{} {}'.format(tc, ans))
