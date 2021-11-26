def make_set(x):
    """
    유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
    """
    p[x] = x                            # 노드 x의 부모 저장

def find_set(x):
    """
    x를 포함하는 집합을 찾는 연산
    """
    if p[x] != x:                       # x가 루트가 아닌 경우
        p[x] = find_set(p[x])           # 다시 루트 찾아서 재귀 호출
    return p[x]                         # x의 대표값 반환

def union(x, y):
    """
    x와 y를 포함하는 두 집합을 통합하는 연산
    """
    p[find_set(y)] = find_set(x)        # y의 대표자를 x의 대표자로 변경

def kruskal():
    global ans                          # 최종 가중치 누적
    cnt = idx = 0                       # cnt(간선 선택 개수 -> V개 선택) / idx (제어 변수 while문을 위함)
    while cnt != V:                     # 선택한 간선의 수(cnt)가 전체 정점의 수(V)와 같아지기 전까지(신장 트리 조건) or cnt < V:
        x = edges[idx][0]               # 간선 정보에서 두 정점을 찾아
        y = edges[idx][1]
        if find_set(x) != find_set(y):  # 두 점의 대표 원소 비교
            union(x, y)                 # 같은 그룹이 아닐 때만 union (대표자가 같으면 같은 집합이기 때문에 사이클 형성)
            cnt += 1                    # union을 한 것은 간선을 선택 한 것을 의미
            ans += edges[idx][2]        # 해당 간선의 가중치 누적
        idx += 1                        # 위의 조건문에 관계없이 다음 간선을 선택하기 위해 idx를 증가

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    ans = 0                                     # 가중치의 누적 합
    V, E = map(int, input().split())            # V: 0부터 시작, E: 간선
    edges = [list(map(int, input().split())) for _ in range(E)]
    p = [0] * (V+1)
    """
    아래와 w를 가장 앞으로 밀고 정렬해도 됨!
    tmp = []
    for _ in range(E):
       u, v, w = map(int, input().split())
       tmp.append((w, u, v))
    tmp.sort()
    """
    edges = sorted(edges, key=lambda x: x[2])   # 가중치(인덱스 2번)를 기준으로 정렬

    # p = list(range(V+1))
    for i in range(V+1):
        make_set(i)
    kruskal()
    print('#{} {}'.format(tc, ans))