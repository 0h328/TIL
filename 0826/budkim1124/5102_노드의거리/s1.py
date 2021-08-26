def length(start):
    global result
    Q = []
    Q.append(start)             # queue를 이용해서
    visited[start] = 1          # start 부터 시작이라서
    while Q:                    # Q에서 pop append를 반복하니까
        start = Q.pop(0)        # Q의 첫 요소를 start로 만든다
        for next in range(1, V+1):  #start와 다음 수가 Graph에 있는지 확인하기 위해
            if Graph[start][next] and not visited[next]:    # (start,next) 좌표를 확인하고
                Q.append(next)                  # Q에 다음 노드를 append한다.
                visited[next] = 1               # 방문 기록 남긴다.
                c_list[next] = c_list[start] + 1    # 이전 노드에 비해 경로가 1개 늘었기 때문
                if next == end:                 # end와 같으면 종료
                    result = c_list[next]       # 누적한 c_list의 도착지점 값을 result에 넣는다.
                    return

import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(T):
    V, E = map(int, input().split())

    c_list = [0 for _ in range(V+1)]    # 거리를 찍어주기 위함
    Graph = [[0] * (V+1) for _ in range(V+1)]   # 그래프를 통해 경로를 찍어주려고
    visited = [0 for _ in range(V+1)]   # 방문여부

    for _ in range(E):
        i, j = map(int, input().split())
        Graph[i][j] = 1     
        Graph[j][i] = 1     # 방향이 있는 것이 아니기 때문에 양방향을 고려해야함

    start, end = map(int, input().split())

    result = 0
    length(start)

    print("#{} {}".format(t+1, result))

