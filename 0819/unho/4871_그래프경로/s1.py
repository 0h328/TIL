'''
DFS - 단방향
'''


import sys
sys.stdin = open('input.txt')


def dfs_func(s):
    stack = [s]                             # 스택에 추가

    while stack:                            # 스택이 비어있지 않으면
        node = stack.pop()                  # 스택 제일 위의 값 반환
        if not visited[node]:               # 방문한 적이 없으면
            visited[node] = True            # 방문으로 변경
            for e in vertex_list[node]:     # 단방향으로 연결된 노드 스택에 추가
                stack.append(e)


test_case = int(input())

for tc in range(1, test_case+1):
    v, e = map(int, input().split())
    vertex_list = [[] for _ in range(v+1)]              # 해당 노드가 연결된 노드 리스트 초기화
    visited = [False for _ in range(v+1)]               # 노드별 방문 여부 리스트

    for _ in range(e):                                  # 해당 노드가 연결된 노드들 정리
        vertex1, vertex2 = map(int, input().split())
        vertex_list[vertex1].append(vertex2)


    s, g = map(int, input().split())
    dfs_func(s)                                         # 시작노드 전달하여 dfs 함수 호출

    if visited[g]:                                      # 방문했으면 1, 아니면 0
        answer = 1
    elif not visited[g]:
        answer = 0

    print('#{} {}'.format(tc, answer))