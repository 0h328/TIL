import sys
sys.stdin = open('input.txt')

K = int(input())
arr = [input().split() for _ in range(6)]
direction = [int(a[0]) for a in arr]        # 방향(동, 서, 남, 북)
length = [int(a[1]) for a in arr]           # 길이
max_length = []     # 직사각형 전체 넓이
box_length = []     # 포함되지 않은 직사각형 넓이

for i in range(1, 5):
    if direction.count(i) == 1:         # 직사각형의 변
        max_length.append(length[direction.index(i)])   # 전체 직사각형의 길이 저장
        tmp = direction.index(i) + 3    # 작은 직사각형의 변
        if tmp >= 6:
            tmp -= 6
        box_length.append(length[tmp])

area = max_length[0] * max_length[1] - box_length[0] * box_length[1]
print(K * area)



