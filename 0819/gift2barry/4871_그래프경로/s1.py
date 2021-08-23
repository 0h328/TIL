import sys
sys.stdin = open('input.txt')

# thought process:
# 방향이 있는 그래프, 고로 비 대칭
# 인접행렬 표현식과 스택 자료구조 이용해서 풀어보자

def dfs(v, fin):
    stack = [v]     # 시작 정점을 stack에 넣고 시작

    while stack[-1] != fin:     # 목표지점 찾을때 까지 루프
        v = stack.pop()         # 처음에 시작 stack 이니 빼준다.
                                # (다 방문한 다음 한 발자국 뒤로 간 다음 다시 빈 방 서치하니까)
                                # v 변수에 저장하는 이유는, pop 리턴값을 아래에서 쓰기 위해
        if not visited[v]:      # 아직 미방문 정점이면
            visited[v] = 1      # 방문체크

            for w in range(1, V+1):  # 1번 노드로부터 방문가능한 노드 다 확인
                if G[v][w] == 1 and not visited[w]:     # 미방문상태이고 방문 가능하면
                    stack.append(w)                 # 스택에 push

        if stack == []:         # 더이상 갈 수 있는 방이 없어지면
            return 0            # 0 반환하고 종료

    if stack[-1] == fin:        # 루프 끝나고 현재 위치가 목표지점이면
        return 1                # 1 반환
    else:
        return 0


for tc in range(1, int(input())+1):

    V, E = map(int, input().split())        # 노드와 간선의 갯수 불러오고

    temp = [list(map(int, input().split())) for _ in range(E)]  # 간선 정보 초기화 하고
    # print(temp)

    start, end = map(int, input().split())  # 스타트 & 목표지점

    G = [[0]*(V+1) for _ in range(V+1)]     # 그래프 초기화 하고
    # print(G)

    for i in range(E):                      # 그래프에 노드 숫자 입력
        G[temp[i][0]][temp[i][1]] = 1       # G[1][4] 1표시 로 시작
    # print(G)

    visited = [0 for _ in range(V+1)]       # 방문기록 초기화
    # print(visited)

    print('#{} {}'.format(tc, dfs(start, end)))








