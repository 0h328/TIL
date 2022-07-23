import sys
sys.stdin = open('input.txt')

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
card = list(map(int, sys.stdin.readline().split()))
M = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()
for i in range(M):
    if binary_search(card, check[i], 0, N-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')