# 문제 푼 시간
# 풀이법: Count 사용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    lst = []
    max_l = 0
    # 입력
    for i in range(5):
        temp_lst = list(input())
        max_l = max(max_l, len(temp_lst))
        lst.append(temp_lst)

    ans = ""

    for i in range(max_l):
        for j in range(5):
            try:
                ans += lst[j][i]
            except:
                continue

    print("#{} {}".format(test, ans))