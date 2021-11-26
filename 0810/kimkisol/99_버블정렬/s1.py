import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def BubbleSort(arr, reverse=False):
    if not reverse:
        for i in range(len(arr)- 1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        for i in range(len(arr)- 1, 0, -1):
            for j in range(0, i):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = list(map(int, input().split()))
print(BubbleSort(arr))
print(BubbleSort(arr, True))