'''
미완료
소요시간 1시간 34분
thought process: 27분 53초

다익스트라 알고리즘 try
먼저 인접 행렬 만들고 시작

1. 시작노드에서 접근 가능한 노드 간선의 가중치를 리스트에 입력
2. 접근 가능한 노드간선 중에서, 가장 가중치가 낮은 원소를 선택
3. visit 리스트에 선택된 원소의 인덱스를 체크
4. 2~3번 반복
5. visit에 False 없어지면, 루프 끝
6. N번 인덱스의 원소  == 0번 노드부터 N번 노드 까지의 최소거리 (가중치)

방향성 그래프다
'''

import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())    # 목표지점, 간선 개수
    G = [[1000] * (N + 1) for _ in range(N + 1)]
    visited = [False] * (N + 1)
    ans_list = [0] + ([1000] * N)

    for i in range(E):                  # 노드 간선 관계를 인접행렬로 구현
        s, e, w = map(int, input().split())
        G[s][e] = w

    city = 0
    while False in visited:                     # 모든 노드의 최소 가중치 구할때 까지 반복

        visited[city] = True                    # 방문체크
        next_city = G[city].index(min(G[city])) # 다음 방문 city 결정
        ans_list[next_city] = ans_list[city] + min(G[city])      # 다음 위치의 가중치 (지금까지의 최소 가중치 + 현위치에서 다음까지의 최소 가중치)를 ans_list에 저장
        city = next_city                        # 다음 위치를 현재 위치로 변환

    print(ans_list[N])



