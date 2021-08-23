# 문제 푼 시간
# 풀이법: Count 사용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test = int(input())

for i in range(1, test + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.reverse()

    ans = 0
    max_price = 0

    # 뒤에서부터 시작하여 높은 판매가격 기준으로 낮게 구매할 수 있는 지점
    for price in lst:
        if price > max_price:
            max_price = price
        else:
            ans += max_price - price

    print(f"#{i} {ans}")