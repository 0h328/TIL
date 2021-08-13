import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

t = int(input())

for test in range(1, t + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    ans = float("-inf")

    for i in range(n - m + 1):  # 이동가능 범위 내에서 파리 잡기
        for j in range(n - m + 1):
            temp_max = 0
            for k in range(m):
                temp_max += sum(lst[i + k][j : j + m])

            if temp_max > ans:  # 최대값 변환
                ans = temp_max

    print("#{} {}".format(test, ans))
