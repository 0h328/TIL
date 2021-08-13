import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 이진 탐색 기본

def binary_search(numbers, target):
   lc = 0
   rc = len(numbers) - 1
   while lc <= rc:
       c = (lc + rc) // 2
       if target == c:
           return True
       elif target > c:
           lc = c + 1
       elif target < c:
           rc = c - 1
   return False

numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False

