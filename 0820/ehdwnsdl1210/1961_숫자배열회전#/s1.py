import sys
sys.stdin = open('input.txtx')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ range(N)]




# 90도만 만들줄알면 횟수증가(1,2,3번)
# 90 / [N-1-j][i]
# 180 / [N-1-i][N-1-j]
# 270 / [j][N-1-i]