# 퀵정렬 - 가변 배열 활용 (파이썬스러운 방식)

def quick_sort(numbers):
    N = len(numbers)                                # 길이
    if N <= 1:                                      # 1 이하면 정렬 요소가 없으니
        return numbers                              # 해당값 반환
    pivot = numbers[0]                              # 첫 번째 요소를 pivot으로 잡고
    left, right = [], []                            # 왼쪽 & 오른쪽 주고
    for idx in range(1, N):                         # pivot 다음부터 끝까지 인덱스를 돌며
        if numbers[idx] > pivot:                    # pivot 보다 크면 오른쪽
            right.append(numbers[idx])              # 작거나 같으면 왼쪽 리스트에 넣자
        else:
            left.append(numbers[idx])
    sorted_left = quick_sort(left)                  # 왼쪽을 다시 quick sort
    sorted_right = quick_sort(right)                # 오른쪽을 다시 quick sort
    return [*sorted_left, pivot, *sorted_right]     # 모든 요소에 대한 정렬이 끝나면 unpacking & 하나의 리스트로 처리

numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
# numbers = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

print('정렬 전')
print(numbers)

result = quick_sort(numbers)

print('---------------------------------')
print('정렬 후')
print(result)