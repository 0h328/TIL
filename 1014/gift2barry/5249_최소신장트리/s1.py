'''
총 풀이시간 2시간 5분 39초
디버깅 30분
thought process: 23분 20초

바로 크루스칼 알고리즘 활용해보자

1. 가중치를 오름차순으로 정렬
2. 신장트리 조건인 간선 개수 (노드개수 - 1) 만큼 정점 방문 가능 여부를 확인하는데
3. 끝나는 원소의 대표원소 = 시작하는 원소로 저장
4. 두 노드의 대표원소가 같다면, 스킵 (사이클이 만들어져버림)
4. 노드개수 - 1 만큼 방문하면 끝. 총 가중치의 합 == 답
'''

import sys
sys.stdin = open('input.txt')


def unite(x, y):
    daepyo_y = find_set(y)
    daepyo_x = find_set(x)
    my_list[daepyo_y] = daepyo_x
    return

def make_set(x, y):
    my_list[x] = x
    my_list[y] = y
    return

def find_set(v):
    idx = my_list[v]
    while idx != v:
        v = idx
        idx = my_list[v]
    return idx


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    tmp = [list(map(int, input().split())) for _ in range(E)]
    G = sorted(tmp, key=lambda x: x[2])     # 가중치를 기준으로 인풋 간선 정보 정렬
    my_list = [0] * (V+1)                   # 노드의 숫자는 2까지, but 0을 포함, 고로 총 노드 숫자는 3개: V+1
    ans = 0

    for i in range(E):                      # 모든 정점 집합 만큼
        make_set(G[i][0], G[i][1])          # 간선 집합 생성(해당 원소 집합의 대표원소 지정)

    cnt, j = 0, 0
    while cnt != V:                         # 최소 신장트리가 완성 될 때 까지 루프
        if find_set(G[j][0]) != find_set(G[j][1]):      # 두 정점 집합의 대표원소가 같지 않는 경우에만
            unite(G[j][0], G[j][1])                     # 출발정점의 대표원소를 도착원소의 대표원소로 변경
            ans += G[j][2]                  # 가중치 더해주기
            cnt += 1                        # 확정 간선 개수+1
        j += 1
    print('#{} {}'.format(tc, ans))





