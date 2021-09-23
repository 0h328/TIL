# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    queue = []

    # 트리생성
    for _ in range(m):
        node, v = map(int, input().split())
        tree[node] += v
        queue.append(node)

    # bfs
    while queue:
        e = queue.pop(0)

        # 선택적 종료조건
        if e < l // 2:
            break

        parent = e // 2
        if not tree[parent]:
            queue.append(parent)
        tree[parent] += tree[e]

    ans = tree[l]

    print("#{} {}".format(test, ans))
