from heapq import *
from collections import defaultdict


def prim(start_node, edges):
    # 최소 신장 트리 정보를 담을 배열
    mst = []
    mst_length = 0
    # 인접 간선
    adjacent_edges = defaultdict(list)
    # 인접 간선을 모두 저장
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    # 연결된 노드를 집합으로 표시
    connected_nodes = set()
    connected_nodes.add(start_node)
    # 선택 가능한 간선 리스트를 시작 노드에 연결된 간선들로 초기화
    candidate_edge_list = adjacent_edges[start_node]
    # 선택 가능 간선 리스트를 힙으로 만듦
    heapify(candidate_edge_list)

    # 선택 가능 간선 리스트가 없을 때까지
    while candidate_edge_list:
        # 우선순위 큐에서 가장 최소가 되는 간선을 꺼내온다.
        weight, n1, n2 = heappop(candidate_edge_list)
        # 도착지점 노드가 연결되어 있지 않다면 연결하고,
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            # 최소 신장 트리에 해당 간선을 채워넣는다.
            mst.append((weight, n1, n2))
            mst_length += weight

            # 만약 연결된 노드의 인접 간선 중에서 연결되지 않은 노드를 대상으로 하는 간선이 존재할 경우
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    # 해당 노드를 선택 가능 간선에 추가
                    heappush(candidate_edge_list, edge)

    return mst_length