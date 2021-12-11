import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])

print(min(arr[N-1]))

# arr[1][0] = 49 + 40 = 89
# arr[1][1] = 60 + 26 = 86
# arr[1][2] = 57 + 26 = 83

# arr[2][0] = 13 + 83 = 96
# arr[2][1] = 89 + 83 = 172
# arr[2][2] = 99 + 86 = 185
