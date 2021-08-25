# 참고 -> 파이썬의 리스트가 아닌 포인터를 활용한 방식
# https://ko.wikipedia.org/wiki/%ED%80%B5_%EC%A0%95%EB%A0%AC
def partition(arr: list, start: int, end: int) -> int:
    pivot = arr[start]             # pivot을 선택하는 방법은 여러가지가 있음
    left = start + 1               # pivot 다음 값을 왼쪽 포인터의 시작
    right = end                    # 가장 끝 값을 오른족 포인터의 시작
    done = False                   # 검색 여부를 판단 할 flag

    while not done:
        # 만약 왼쪽 포인터가 오른쪽보다 크지 않고 쪽 포인터가 가리키는 값이 pivot보다 작거나 같으면
        # 왼쪽 포인터는 pivot보다 큰 값을 만날 때까지 이동
        while left <= right and arr[left] <= pivot:
            left += 1
        # 만약 왼쪽 포인터가 오른쪽보다 크지 않고 오른쪽 포인터가 가리키는 값이 pivot보다 크거나 같으면
        # 오른쪽 포인터는 pivot보다 작은 값을 만날 때까지 이동
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left: # 만약 포인터의 위치가 바뀐다면(cross 된다면) 종료
            done = True
        else:            # 포인터의 위치가 바뀌지 않는다면 왼쪽과 오른쪽 포인터가 가리키고 있는 값을 바꾸자
            arr[left], arr[right] = arr[right], arr[left]
    # 반복이 다 끝나고 시작 포인터의 값과 오른쪽 포인터의 값을 교환하자
    # pivot 값을 기준으로 왼쪽과 오른쪽이 각각 작고/큰으로 정렬됨을 알 수 있음
    arr[start], arr[right] = arr[right], arr[start]
    # 최종적으로 해당 pivot 값을 반환
    return right


def quick_sort(arr: list, start: int, end: int) -> list:
    # 호출이 한번 진행될 때마다 최소한 하나의 원소(피벗)는 최종적으로 위치가 정해지므로
    # 이 알고리즘은 반드시 끝난다는 것을 보장할 수 있다.
    if start < end:
        pivot = partition(arr, start, end)  # pivot 결정
        quick_sort(arr, start, pivot - 1)   # pivot을 기준으로 왼쪽을 정렬
        quick_sort(arr, pivot + 1, end)     # pivot을 기준으로 오른쪽을 정렬
    return arr                              # 정렬이 모두 끝났으면 해당 리스트를 반환

# 고정 배열
import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums, 0, len(nums)-1))