# 문제 푼 시간
# 풀이법: dfs
from collections import deque


def dfs(x: int, y: int):
    global ans
    global temp

    if x == n - 1:  # 종료조건
        if temp < ans:
            ans = temp
        return

    for i in range(n):
        if not visited[i]:
            temp += mp[x + 1][i]
            if temp < ans:  # 여전히 최소값보다 작을 경우
                visited[i] = 1
                dfs(x + 1, i)
                visited[i] = 0  # 이전 값으로 복귀
            temp -= mp[x + 1][i]  # 이전 값으로 복귀


import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    ans = 10 * n

    for i in range(n):  # 위에서부터 탐색 시작
        temp = mp[0][i]  # 합계 초기화
        visited = [0] * n  # 방문표시 초기화
        visited[i] = 1
        dfs(0, i)

    print("#{} {}".format(test, ans))
