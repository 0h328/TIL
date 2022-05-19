import sys
from collections import Counter
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())
    wear = []

    for i in range(n):
        cloth, body = input().split()
        wear.append(body)

    wear_counter = Counter(wear)  # 리스트 안에 중복되는 요소를 key: 요소, value: 개수 형식으로 count해줌
    cnt = 1
    # print(wear_counter)

    for key in wear_counter:
        cnt *= wear_counter[key] + 1

    print(cnt-1)