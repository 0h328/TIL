import sys
sys.stdin = open('input.txt')

def dfs(v, fin):
    stack = [v]                         # 시작 정점을 stack에 넣고 시작

    while stack[-1] != fin:             # 목표지점 찾을때 까지 루프
        v = stack.pop()                 # 시작 node에 진입했으니 pop

        if visited[v] != 1:             # 미방문 node 일때
            visited[v] = 1              # 입실체크

            for w in range(1, 100+1):   # 1번 node 부터 방문 가능한 node 다 검색
                if G[v][w] == 1 and visited[w] != 1:    # 미방문 & 방문가능하면
                    stack.append(w)                     # 해당 node stack에 push
        if stack == []:                 # 더이상 갈 수 있는 방이 없으면
            return 0                    # 0반환하고 종료

    if stack[-1] == fin:                # 루프 끝나고 현위치가 목표지점이면
        return 1                        # 1 반환
    else:
        return 0


for tc in range(1, 10+1):
    T, E = map(int, input().split())    # 테스트idx, 간선 개수

    temp = [x+1 for x in list(map(int, input().split()))]   # 인풋 순서쌍들에 + 1 (계산 편하게하려고)
                                                            # 간선 정보 초기화
    cnt = set(temp)
    V = len(cnt)           # 노드 개수 계산

    G = [[0] * (100+1) for _ in range(100+1)]   # 그래프 초기화, 100 node 까지 존재, 고로 그래프도 최대 100x100

    for i in range(E):                          # 그래프에 node 입력
        G[temp[i*2]][temp[i*2+1]] = 1
    # print(G)

    visited = [0] * (100+1)                     # 방문기록 초기화

    print('#{} {}'.format(T, dfs(1, 100)))        # 시작점과 종착점은 항상 1, 100 고정

