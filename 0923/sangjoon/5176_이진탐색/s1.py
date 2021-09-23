# 문제 푼 시간
# 풀이법: 중위 탐색
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    tr = {}
    for i in range(1, n+1):
        if i//2 in tr:
            tr[i//2].append(i)
        tr[i] = []

    ans = [0, 0]
    cnt = 0

    # 중위 탐색
    def inorder_traverse(node: int):
        global cnt

        # 왼쪽 탐색
        if tr[node]:
            inorder_traverse(tr[node][0])

        # 중위 탐색
        cnt += 1
        if node == 1:
            ans[0] = cnt
        if node == n//2:
            ans[1] = cnt

        # 오른쪽 탐색
        if len(tr[node]) > 1:
            inorder_traverse(tr[node][1])

    inorder_traverse(1)

    print("#{} {} {}".format(test, ans[0], ans[1]))
