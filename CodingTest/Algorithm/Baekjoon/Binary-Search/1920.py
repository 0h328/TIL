import sys
sys.stdin = open('input.txt')

# 풀이1
# N = int(input())
# numbers = list(map(int, input().split()))
# numbers.sort()
# M = int(input())
# target = list(map(int, input().split()))
#
# def binarySearch(numbers, t):
#     start = 0
#     end = len(numbers) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#         if t == numbers[mid]:
#             return 1

#         elif t > numbers[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return 0
#
# for t in target:
#     print(binarySearch(numbers, t))

# 풀이2
N = int(sys.stdin.readline().strip())
numbers = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
target = map(int, sys.stdin.readline().split())

for t in target:
    if t in numbers:
        print(1)
    else:
        print(0)

