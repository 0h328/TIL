# 문제 푼 시간
# 풀이법: permutaion 사용
import pathlib, sys
from itertools import combinations

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def check_cnt(a, b):
    global min_cnt
    cnt = 0

    for i in range(0, a):  # 0~a-1 까지 칠해야할 W 개수
        cnt += flag_dic[i]["W"]

    for i in range(a, b):  # a~b-1 까지 칠해야할 B 개수
        cnt += flag_dic[i]["B"]

    for i in range(b, n):  # b~n-1 까지 칠해야할 R 개수
        cnt += flag_dic[i]["R"]

    if cnt < min_cnt:
        min_cnt = cnt


test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())

    flag_dic = {i: {} for i in range(n)}
    for i in range(n):  # 줄에서 색상별 칠해야 할 개수 초기화
        word = list(input())
        flag_dic[i]["W"] = m - word.count("W")
        flag_dic[i]["B"] = m - word.count("B")
        flag_dic[i]["R"] = m - word.count("R")

    min_cnt = m * n  # 최소값 초기화
    point = [i for i in range(1, n)]  # idx: 0은 무조건 흰색이다. 이외 2개의 분기점이 존재해야 한다.
    point_sets = list(combinations(point, 2))  # 조합 생성

    for a, b in point_sets:
        check_cnt(a, b)

    print("#{} {}".format(test, min_cnt))
