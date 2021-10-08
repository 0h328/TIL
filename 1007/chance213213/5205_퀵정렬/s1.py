'''
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램
'''

import sys
sys.stdin = open('input.txt')

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    res = False
    while not res:
        while left <= right and arr[left] <= pivot: #가장 오른쪽에 위치한 pivot 보다 작은 수 찾기
            left += 1
        while left <= right and arr[right] >= pivot:#가장 왼쪽에 위치한 pivot 보다 큰 수 찾기
            right -= 1
        if left > right: #교차
            res = True #while 끝내줘야 됨
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start] # 어 이건 왜 바꾸더라?
    return right # 왜 right 출력하더라?

def quick_sort(arr, start, end):
    if start < end: #정상 범위
        pivot = partition(arr, start, end) #partition에서 반환되는 right, 인덱스 아님??
        quick_sort(arr, start, pivot-1) #이건 왼쪽 그룹 보기
        quick_sort(arr, pivot+1, end) #다시 돌아왔을 땐, 오른쪽 부분 보기
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = quick_sort(numbers, 0, len(numbers)-1) # 처음과 끝 index 넣어줌
    print('#{} {}'.format(tc, result[N//2]))

    #아 교수님이 1개 케이스 통과 못한다고 했는데, 어떻게 하라고 했더라?