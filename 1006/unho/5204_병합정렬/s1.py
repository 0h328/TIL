import sys
sys.stdin = open('input.txt')


def merge(left, right):
    global answer 

    sorted_list = []                # 정렬 리스트
    L = R = 0                       # 왼쪽 / 오른쪽 인덱스

    if left[-1] > right[-1]:
        answer += 1

    while L < len(left) and R < len(right):       # 정렬된 리스트의 크기가 왼쪽과 오른쪽 분할 리스트와 같아 질때까지 반복 작업
        if left[L] <= right[R]:                             # 오른쪽이 크면 왼쪽을 먼저 넣고
            sorted_list.append(left[L])                     # 왼쪽 인덱스 증가
            L += 1
        else:                                               # 왼쪽이 크면 오른쪽을 먼저 넣고
            sorted_list.append(right[R])                    # 왼쪽을 먼저 넣고
            R += 1                                          # 오른쪽 인덱스 증가
            
    if R == len(right):             # 오른쪽 인덱스의 범위가 배열 크기를 넘어가면 (오른쪽 요소의 정렬이 끝나 왼쪽이 남았다는 말)
        sorted_list += left[L:]     # 왼쪽의 나머지 것을 모두 뒤에 붙이고(해당하는 요소는 적어도 현재 sorted_list에 있는 요소 보다는 클 것)
    else:
        sorted_list += right[R:]

    return sorted_list

def partition(nums):
    if len(nums) < 2:               # 1개 이하로 남으면 반환
        return nums 

    left = partition(nums[:len(nums) // 2])    # 왼쪽 
    right = partition(nums[len(nums) // 2:])   # 오른쪽으로 구분

    return merge(left, right)       # merge 함수 호출


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    answer = 0

    result = partition(li)

    print('#{} {} {}'.format(tc, result[N//2], answer))