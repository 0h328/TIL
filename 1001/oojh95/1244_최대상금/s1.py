import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    data, cnt = int(input().split())
    arr = []
    while data > 0:
        arr.append(data//10)
        data //= 10
    arr = arr[::-1]
    for i in range(cnt+1):

