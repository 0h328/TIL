import sys

sys.stdin = open('input.txt')
'''
B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수
'''

def binary_search(t_start, t_end, start, end, state):
    global res, x, y
    p1 = p2 = -1
    if start <= end and t_start <= t_end:
        mid = start + (end - start) // 2
        for i in range(t_start, t_end):
            if nums[mid] == targets[i]:
                res += 1
                if i > 0 and targets[i] != targets[i - 1]:
                    p1 = i
            elif nums[mid] < targets[i]:
                p2 = i
                break
        if p1 == -1:
            p1 = p2
        if state != 'L':
            binary_search(t_start, p1, start, mid - 1, 'L')
        if state != 'R':
            binary_search(p2, t_end, mid + 1, end, 'R')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 찾아야 될 곳의 숫자 개수, M : 찾을 숫자 개수
    nums = sorted(list(map(int, input().split())))  # POINT) 문제 잘 읽기. 문제가 불친절하긴 했음 마치 sorted된걸 주는 것처럼 설명해놓음
    targets = sorted(list(map(int, input().split())))
    res = 0
    binary_search(0, len(targets), 0, len(nums) - 1, 'M')

    print('#{} {}'.format(t, res))

# def binary_search_iteration(nums, target, start, end):
#     global res
#     state = ''
#     while start <= end:
#         mid = start + (end - start) // 2
#         if nums[mid] == target:
#             res += 1
#             return
#         elif nums[mid] < target:
#             if state == 'R':
#                 return
#             start = mid + 1
#             state = 'R'
#         else:
#             if state == 'L':
#                 return
#             end = mid - 1
#             state = 'L'
#
# T = int(input())
#
# for t in range(1, T + 1):
#     N, M = map(int, input().split())  # N: 찾아야 될 곳의 숫자 개수, M : 찾을 숫자 개수
#     nums = sorted(list(map(int, input().split())))
#     targets = list(map(int, input().split()))
#     res = 0
#
#     for target in targets:
#         start = 0
#         end = len(nums) - 1
#         binary_search_iteration(nums, target, start, end)
#
#     print('#{} {}'.format(t, res))
