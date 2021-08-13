import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    red = [[0] * 10 for _ in range(10)]  # 같은색 끼리 겹칠 수 있기 때문에
    blue = [[0] * 10 for _ in range(10)]  # 두 가지 색에 대해 방문리스트 생성
    ans = 0

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1:  # 빨간색일 경우 방문표시
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    red[i][j] = 1

        if color == 2:  # 파란색일 경우 방문표시
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    blue[i][j] = 1

    for i in range(10):  # 두가지 색 모두 방문 표시 되었을 경우
        for j in range(10):
            if red[i][j] == 1 and blue[i][j] == 1:
                ans += 1

    print("#{} {}".format(test, ans))
