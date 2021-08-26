# 문제 푼 시간
# 풀이법: Count 사용
import collections
import pathlib, sys


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def bfs(x: int, y: int):
    pass


test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input().split())
    mp = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if mp[i][j] == 2:
                bfs(i, j)

    print("#{} {}".format(test, ans))