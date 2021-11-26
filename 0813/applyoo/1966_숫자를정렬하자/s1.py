import sys
sys.stdin = open('input.txt', encoding='UTF8')


def qsort(arr):  # 퀵 정렬
    if len(arr) < 2:  # Base Case
        return arr

    pivot = arr[len(arr) // 2]  # 대부분의 배열이 어느 정도 정렬돼있다는 가정하에 중간으로 지정
    arr.remove(pivot)  # 해당 pivot을 정렬에서 제거하지 않으면 무한 재귀가 됨

    left = [i for i in arr if i <= pivot]  # pivot보다 작거나 같은 값을 저장하는 리스트
    right = [i for i in arr if i > pivot]  # pivot보다 큰 값을 저장하는 리스트

    return qsort(left) + [pivot] + qsort(right)  # 3개의 리스트를 더하여 return함


T = int(input())
for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    sort_arr = qsort(arr)
    print('#{}'.format(test+1), end=' ')
    print(*sort_arr)