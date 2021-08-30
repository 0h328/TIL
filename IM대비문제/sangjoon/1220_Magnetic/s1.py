# 문제 푼 시간
# 풀이법: 스택을 활용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = 10

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        stack = []  # 스택초기화
        for j in range(n):  # 위에서부터 탐색
            if mp[j][i] == 1:  # N극일 경우
                stack.append(1)

            elif mp[j][i] == 2:  # S극일 경우
                if stack:
                    stack.clear()  # 쌓인 N극 초기화
                    ans += 1  # 교착상태 추가

    print("#{} {}".format(test, ans))
