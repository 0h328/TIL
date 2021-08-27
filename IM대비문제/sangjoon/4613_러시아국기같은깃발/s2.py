# 문제 푼 시간
# 풀이법: dfs사용 # 실패
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dfs(line: int, cnt: int):
    global min_cnt
    global start_blue
    global end_blue

    if line == n - 1:
        if cnt < min_cnt and start_blue:  # 파란이 칠해진 경우
            min_cnt = cnt
        return

    if not start_blue:  # 위에서 부터 파란색이 칠해지기 전 가능 조합
        color_lst = ["W", "B"]
    elif not end_blue:  # 파란색이 칠해진 후 가능한 조합
        color_lst = ["B", "R"]
    else:  # 빨간색이 칠해진 후 가능 한 조합
        color_lst = ["R"]

    for color in color_lst:
        if color == "B":  # 파란색을 칠한 경우
            start_blue = True
        if color == "R":  # 빨간색을 칠한 경우
            end_blue = True

        cnt_c = m - lst[line].count(color)  # 칠해야할 색상 개수
        cnt += cnt_c
        if cnt < min_cnt:  # 작을 경우에만 탐색
            dfs(line + 1, cnt)
        cnt -= cnt_c


test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    lst = [list(input()) for _ in range(n)]
    ans = m * 2 - lst[0].count("W") - lst[n - 1].count("R")
    min_cnt = m * n
    start_blue, end_blue = False, False

    dfs(1, ans)

    print("#{} {}".format(test, min_cnt))
