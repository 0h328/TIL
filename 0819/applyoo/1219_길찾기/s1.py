import sys
sys.stdin = open('input.txt')


def dfs(node):
    global result
    if node == 99:  # 찾는 노드는 99임
        result = 1  # 찾았으므로 1로 변경
        return
    visited[node] = True  # 방문 표시

    for next_node in node_map[node]:  # 해당 노드의 인접 리스트 반복
        if not visited[next_node]:  # 방문을 안한 경우
            dfs(next_node)  # 다음 노드 재귀


for _ in range(10):
    test, N = map(int, input().split())
    arr = list(map(int, input().split()))
    node_map = [[] for _ in range(100)]
    visited = [False] * 100  # 방문을 표시할 리스트
    result = 0  # 방문 가능 여부를 표시할 변수

    for i in range(N):
        node_map[arr[2*i]].append(arr[2*i+1])
    dfs(0)

    print('#{} {}'.format(test, result))
