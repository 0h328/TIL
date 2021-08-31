# 문제 푼 시간
# 풀이법: dfs -> 실패

# 다시 고쳐야할 필요 있음

import pathlib, sys
from itertools import combinations

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dfs(line: int, cnt: int):
    global min_cnt
    global end_white
    global end_blue

    if line == n - 1:
        if cnt < min_cnt and end_white:
            min_cnt = cnt
        return

    if not end_white:
        color_lst = ["W", "B"]
    elif not end_blue:
        color_lst = ["B", "R"]
    else:
        color_lst = ["R"]

    for color in color_lst:
        if color == "B":
            end_white = True
        if color == "R":
            end_blue = True

        cnt_c = flag_dic[line][color]
        cnt += cnt_c
        dfs(line + 1, cnt)
        cnt -= cnt_c

        if color == "B":
            end_white = False
        if color == "R":
            end_blue = False


test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    flag_dic = {i: {} for i in range(n)}

    for i in range(n):
        word = list(input())
        flag_dic[i]["W"] = m - word.count("W")
        flag_dic[i]["B"] = m - word.count("B")
        flag_dic[i]["R"] = m - word.count("R")

    print(flag_dic)
    ans = flag_dic[0]["W"] + flag_dic[n - 1]["R"]
    min_cnt = m * n
    end_white, end_blue = False, False

    dfs(1, ans)

    print("#{} {}".format(test, min_cnt))
