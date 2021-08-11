from itertools import count
import sys

sys.stdin = open("input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    ans, cnt = 0, 0
    n, num = int(input()), int(input())
    counter = [0] * 10  # 숫자별 카운터 리스트 생성

    while num > 0:
        num, card = divmod(num, 10)
        counter[card] += 1  # 숫자별 개수 추가

    for num in range(10):
        num_cnt = counter[num]
        if num_cnt >= cnt:
            ans, cnt = num, num_cnt  # 최대 개수 및 숫자

    print("#{} {} {}".format(test, ans, cnt))