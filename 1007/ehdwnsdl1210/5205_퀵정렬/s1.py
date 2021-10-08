'''
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력
'''

def quick_sort(array):
    if len(array) <= 1:     # 리스트가 하나 이하의 원소만을 담고 있으면 종료
        return array

    pivot = array[0]        # 피벗은 첫 번째 원소
    tail = array[1:]        # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]     # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = quick_sort(arr)

    print(f'#{tc} {arr[N//2]}')


#1 2
#2 6
