# 문제 푼 시간
# 풀이법: 누적합 사용
import pathlib, sys
from collections import Counter

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    buy = 0  # 총 구매 개수

    counter = Counter(lst)  # Counter 연산
    counter = sorted(counter.items(), key=lambda x: x[0])  # Counter key 값 기준 Sort
    ans = "Possible"

    for t, num in counter:  # 시간과 구매자 수를 순회
        sell = k * (t // m)  # 시간대 기준 총 판매가능 개수
        buy += num  # 시간대 기준 누적 구매량
        if buy > sell:
            ans = "Impossible"
            break

    print("#{} {}".format(test, ans))