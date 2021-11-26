# 문제 푼 시간
# 풀이법: Count 사용
import pathlib, sys
from itertools import combinations


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    comb_lst = combinations(lst, 2)  # 두개 숫자에 대한 조합 생셩
    ans = -1  # 단조증가가 없을 경우

    for a, b in comb_lst:
        temp = str(a * b)
        prev = temp[0]
        is_mono = True
        for i in range(1, len(temp)):
            if prev > temp[i]:  # 단조증가가 성립하지 않을 경우
                is_mono = False
                break
            prev = temp[i]
        if is_mono:  # 단조증가 숫자일 경우
            if int(temp) > ans:
                ans = int(temp)

    print("#{} {}".format(test, ans))