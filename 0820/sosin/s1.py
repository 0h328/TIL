# N = 3
# arr = [[1, 2, 3, 1, 2, 3],
# [4, 5, 6, 4, 5, 6],
# [4, 9, 0, 4, 9, 0]]
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))*2
for i in range(N-1):
    temp = tuple(map(int, input().split()))*2
    arr[0] += max(temp[1], temp[0])
    arr[1] += max(temp[0], temp[1], temp[2])
    arr[2] += max(temp[1], temp[2])

    arr[3] += min(temp[3], temp[4])
    arr[4] += min(temp[4], temp[5], temp[3])
    arr[5] += min(temp[4], temp[5])

print(max(arr), min(arr))