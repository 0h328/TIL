'''
DFS - 단방향
시간 단축
'''

import sys
sys.stdin = open('input.txt')



def dfs_func(start):
    stack = [start]                                     # 시작 노드 스택에 추가

    while stack:
        node = stack.pop()                              # 노드 값 꺼내기
        if not visited[node]:                           # 방문한적 없으면 방문 리스트 True 로 변경
            visited[node] = True
            if linked1[node]:                           # 연결된 노드들 있으면 추가
                tmp1 = linked1[node]
                stack.append(tmp1)
            if linked2[node]:
                tmp2 = linked2[node]
                stack.append(tmp2)
        if tmp1 == 99 or tmp2 == 99:
            visited[99] = True
            break



for _ in range(1, 11):
    tc, edge = map(int, input().split())
    in_link = input().split()                                           # 입력받은 연결 관련 문자열
    visited = [False] * 100                                             # 방문 여부 1차원 리스트로 초기화
    linked1 = [0] * 100                                                 # 단방향 연결된 노드들 저장할 리스트
    linked2 = [0] * 100

    for i in range(len(in_link)//2):                                    # 노드들 연결 관계 정리
        vertex1, vertex2 = int(in_link[i*2]), int(in_link[i*2 + 1])     # 하나의 노드 출발 - 도착
        if not linked1[vertex1]:                                        # 첫번째 연결 리스트의 값이 0이라면 추가
            linked1[vertex1] = vertex2
        else:                                                           # 첫번째에 값이 있으면 두번째에 저장
            linked2[vertex1] = vertex2

    dfs_func(0)

    if visited[99]:                                                     # 방문 했으면 1
        answer = 1
    elif not visited[99]:
        answer = 0

    print('#{} {}'.format(tc, answer))
