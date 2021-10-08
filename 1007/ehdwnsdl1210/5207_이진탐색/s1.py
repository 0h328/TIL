'''
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장
그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.

전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면,
중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r

이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.
'''


'''
연습 문제3. 이진 탐색
 - 이진 탐색을 반복문과 재귀 함수를 활용하여 구현하시오.
 - 찾고자 하는 값(target)이 있다면 해당 값의 인덱스를 없다면 -1을 반환하시오.


#1. iteration
def binary_search_iteration(nums, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2            # 가운데 값을 찾고
        if nums[mid] == target:                     # 값을 찾은 경우
            return mid                              # 해당 인덱스(mid) 반환
        elif nums[mid] < target:                    # target이 더 크면
            start = mid + 1                         # 왼쪽을 버리자 (start를 mid + 1로 이동)
        else:                                       # target이 더 작으면
            end = mid - 1                           # 오른쪽을 버리자 (end를 mid - 1로 이동)
    return -1                                       # 못찾은 경우 -1

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 2       # 있는 경우 -> 있는 값의 인덱스
# target = 90    # 없는 경우 -> -1

start = 0
end = len(nums) - 1
find_val = binary_search_iteration(nums, target, start, end)

if find_val == -1:
    print('{}(은)는 없습니다.'.format(target))
else:
    print('{}(은)는 {}번째에 있습니다.'.format(target, find_val))


#2. recursion
def binary_search_recursion(nums, target, start, end):
    if end >= start:
        mid = start + (end - start) // 2
        if nums[mid] == target:                                             # 값을 찾으면 return 하자
            return mid
        elif nums[mid] > target:                                            # 왼쪽에서 찾고   
            return binary_search_recursion(nums, target, start, mid-1)      # end를 mid-1로 설정
        else:                                                               # 오른쪽에서 찾자
            return binary_search_recursion(nums, target, mid+1, end)        # start를 mid+1로 설정
    else:
        return -1                                                           # 못찾으면 -1 반환

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 2
# target = 90
start = 0
end = len(nums) - 1

find_val = binary_search_recursion(nums, target, start, end)

if find_val == -1:
    print('{}(은)는 없습니다.'.format(target))
else:
    print('{}(은)는 {}번째에 있습니다.'.format(target, find_val))
'''


def binary_search_recursion(nums, target, start, end):
    global cnt
    global result

    if abs(cnt[0] - cnt[1]) > 1:
        return

    if end >= start:
        mid = (start + end) // 2
        if nums[mid] == target:  # 값을 찾으면 return 하자
                result += 1
                return

        elif nums[mid] > target and cnt[0] > 0:  # 왼쪽에서 찾고
            # if abs(cnt[0] - cnt[1]) == 1 and cnt[0] > 0:
            #     return
            cnt[0] += 1
            binary_search_recursion(nums, target, start, mid - 1)  # end를 mid-1로 설정
        elif nums[mid] < target and cnt[1] > 0:  # 오른쪽에서 찾자
            # if abs(cnt[1] - cnt[0]) == 1 and cnt[1] > 0:
            #     return
            cnt[1] += 1
            binary_search_recursion(nums, target, mid + 1, end)  # start를 mid+1로 설정
    else:
        return


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))

    list_A.sort()

    result = 0

    for i in list_B:
        cnt = [0, 0]
        binary_search_recursion(list_A, i, 0, N-1)

    print(f'#{tc} {result}')


#1 2
#2 0
#3 3
