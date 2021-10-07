# 병합 정렬

def merge(left, right):
    if len(left) == 0:              # 왼쪽 배열이 비어있으면 합칠 게 없기 때문에 오른쪽 반환
        return right
    if len(right) == 0:             # 오른쪽 배열이 비어있으면 합칠 게 없기 때문에 왼쪽 반환
        return left
    sorted_list = []                # 정렬 리스트
    L = R = 0                       # 왼쪽 / 오른쪽 인덱스

    while len(sorted_list) != len(left) + len(right):       # 정렬된 리스트의 크기가 왼쪽과 오른쪽 분할 리스트와 같아 질때까지 반복 작업
        if left[L] <= right[R]:                             # 오른쪽이 크면 왼쪽을 먼저 넣고
            sorted_list.append(left[L])                     # 왼쪽 인덱스 증가
            L += 1
        else:                                               # 왼쪽이 크면 오른쪽을 먼저 넣고
            sorted_list.append(right[R])                    # 왼쪽을 먼저 넣고
            R += 1                                          # 오른쪽 인덱스 증가
                                        # 위에서 증가 시킨 인덱스 -> 이 값이 먼저 찼다는 말은 값이 더 작아서 먼저 sorted_list에 추가되었다는 의미
        if R == len(right):             # 오른쪽 인덱스의 범위가 배열 크기를 넘어가면 (오른쪽 요소의 정렬이 끝나 왼쪽이 남았다는 말)
            sorted_list += left[L:]     # 왼쪽의 나머지 것을 모두 뒤에 붙이고(해당하는 요소는 적어도 현재 sorted_list에 있는 요소 보다는 클 것)
            break                       # 종료

        if L == len(left):              # 왼쪽의 경우도 마찬가지
            sorted_list += right[R:]
            break
    return sorted_list

def partition(nums):
    if len(nums) < 2:               # 1개 이하로 남으면 반환
        return nums 
    mid = len(nums) // 2            # middle 값 찾고
    left = partition(nums[:mid])    # 왼쪽 
    right = partition(nums[mid:])   # 오른쪽으로 구분
    return merge(left, right)       # merge 함수 호출


numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
# numbers = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

print(numbers)                              # 정렬 전
print(partition(numbers))                   # 정렬 후