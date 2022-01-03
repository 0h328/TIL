import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())        # w: 가로의 길이, h: 세로의 길이
N = int(input())                        # 상점의 개수
arr = []

# 1: 북, 2: 남, 3: 서, 4: 동
for _ in range(N):
    d, p = map(int, input().split())    # d: 상점의 방향, p: 상점의 위치
    arr.append((d, p))
d_d, d_p = map(int, input().split())    # d_d: 동근이의 방향, d_p: 동근이의 거리
res = 0                                 # 거리의 합을 구하기 위한 변수

for a in arr:
    if d_d == 1:                        # 동근 위치: 북
        if a[0] == 1:                   # 상점 위치: 북
            res += abs(a[1] - d_p)
        if a[0] == 2:                   # 상점 위치: 남
            res += min(d_p + h + a[1], w-d_p + h + w-a[1])
        if a[0] == 3:                   # 상점 위치: 서
            res += d_p + a[1]
        if a[0] == 4:                   # 상점 위치: 동
            res += w-d_p + a[1]
    if d_d == 2:                        # 동근 위치: 남
        if a[0] == 1:                   # 상점 위치: 북
            res += min(a[1] + h + d_p, w-d_p + h + w-a[1])
        if a[0] == 2:                   # 상점 위치: 남
            res += abs(a[1] - d_p)
        if a[0] == 3:                   # 상점 위치: 서
            res += d_p + h-a[1]
        if a[0] == 4:                   # 상점 위치: 동
            res += w-d_p + h-a[1]
    if d_d == 3:                        # 동근 위치: 서
        if a[0] == 1:                   # 상점 위치: 북
            res += d_p + a[1]
        if a[0] == 2:                   # 상점 위치: 남
            res += h-d_p + a[1]
        if a[0] == 3:                   # 상점 위치: 서
            res += abs(a[1] - d_p)
        if a[0] == 4:                   # 상점 위치: 동
            res += min(d_p + w + a[1], h-d_p + w + h-a[1])
    if d_d == 4:                        # 동근 위치: 동
        if a[0] == 1:                   # 상점 위치: 북
            res += d_p + w-a[1]
        if a[0] == 2:                   # 상점 위치: 남
            res += h-d_p + w-a[1]
        if a[0] == 3:                   # 상점 위치: 서
            res += min(d_p + w + a[1], h-d_p + w + h-a[1])
        if a[0] == 4:                   # 상점 위치: 동
            res += abs(a[1] - d_p)

print(res)