def partition(arr, start, end):
    pass

def quick_sort(arr, start, end):
    pass

# 고정 배열
import sys
sys.stdin = open('input.txt')
numbers = list(map(int, input().split()))
print(quick_sort(numbers, 0, len(numbers)-1))