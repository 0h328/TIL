"""
교수님의 합병정렬 코드를 디버깅하며 참고하였습니다.
잘개 쪼여질 때 배열의 크기가 1일때 반환되므로, 합병할 때 배열의 크기가 0인지 확인할 필요는 없습니다.
"""
import sys
sys.stdin = open('input.txt')


def divide(nums):
    global cnt
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = divide(nums[:mid])
    right = divide(nums[mid:])
    if left[-1] > right[-1]:
        cnt += 1
    return conquer(left, right)


def conquer(left, right):
    sorted_list = []
    L = R = 0

    while len(sorted_list) != len(left) + len(right):
        if left[L] <= right[R]:
            sorted_list.append(left[L])
            L += 1
        else:
            sorted_list.append(right[R])
            R += 1

        if R == len(right):
            sorted_list += left[L:]
            break

        if L == len(left):
            sorted_list += right[R:]
            break
    return sorted_list


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))
    cnt = 0
    new_list = divide(my_list)
    mid_num = new_list[N//2]
    print("#{} {} {}".format(test_case, mid_num, cnt))