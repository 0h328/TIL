import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))

    def bubble_sort(arr):
        for l in range(len(arr) -1, 0, -1): # 마지막부터 idx 줄여나감
            for i in range(l):
                if arr[i] > arr[i+1]: # 큰 값이 앞에 있으면 위치 바꿔줌
                    arr[i], arr[i+1] = arr[i+1], arr[i]

    bubble_sort(arr)
    print(arr)