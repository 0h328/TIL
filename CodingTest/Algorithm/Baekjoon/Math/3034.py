import sys
sys.stdin = open('input.txt')

N, W, H = map(int, input().split())
for i in range(N):
    b = int(input())
    l = (W**2 + H**2) ** 0.5
    if b <= l:
        print("DA")
    else:
        print("NE")