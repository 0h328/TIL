# 문제 푼 시간
# 풀이법: 후위탐색
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = 10

for test in range(1, test_case + 1):
    n = int(input())
    tree = {}
    for _ in range(n):
        lst = list(input().split())
        tree[lst[0]] = lst[1:]

    def postorder_traverse(node):
        if len(tree[node]) > 1:
            v1 = postorder_traverse(tree[node][1])
            v2 = postorder_traverse(tree[node][2])
            return str(eval(v1 + tree[node][0] + v2))
        else:
            return tree[node][0]

    ans = postorder_traverse("1")
    ans = int(float(ans))
    print("#{} {}".format(test, ans))
