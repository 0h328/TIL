import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [float(input()) for _ in range(N)]

for i in range(1, N):
    arr[i] = max(arr[i], arr[i-1]*arr[i])

print("{:.3f}".format(max(arr)))