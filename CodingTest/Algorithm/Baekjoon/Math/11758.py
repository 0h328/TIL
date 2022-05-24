import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(3)]

dir_1 = [arr[1][0] - arr[0][0], arr[1][1] - arr[0][1]]
dir_2 = [arr[2][0] - arr[1][0], arr[2][1] - arr[1][1]]

ans = (dir_1[0] * dir_2[1] - dir_1[1] * dir_2[0])

if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)
