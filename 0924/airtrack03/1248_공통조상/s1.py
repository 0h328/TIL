from collections import deque
import sys
sys.stdin = open("input.txt")

T = int(input())

def find_common(queue):
    while queue:
        cur = queue.popleft()

        nxt = tree[cur][2]
        if not nxt:
            continue
        if visited[nxt]:
            return nxt
        queue.append(nxt)
        visited[nxt] = 1

def cnt_subnode(root):
    visited = [0] * (V+1)
    queue = deque()
    queue.append(root)
    cnt = 1
    visited[root] = 1

    while queue:
        cur = queue.popleft()
        left = tree[cur][0]
        right = tree[cur][1]

        if not visited[left] and left:
            queue.append(left)
            visited[left] = 1
            cnt += 1
        if not visited[right] and right:
            queue.append(right)
            visited[right] = 1
            cnt += 1

    return cnt




for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    data = list(map(int, input().split()))

    tree = [[0, 0, 0] for _ in range(V+1)]
    # 루트는 항상 1
    for i in range(E):
        p, c = data[2*i], data[2*i+1]
        if tree[p][0]:
            tree[p][1] = c
        else:
            tree[p][0] = c
        tree[c][2] = p


    visited = [0 for _ in range(V + 1)]
    queue = deque()

    queue.append(n1)
    visited[n1] += 1
    queue.append(n2)
    visited[n2] += 1

    common_node = find_common(queue)

    cnt = cnt_subnode(common_node)

    print('#{} {} {}'.format(tc, common_node, cnt))

