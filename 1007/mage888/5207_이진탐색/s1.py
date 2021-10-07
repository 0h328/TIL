import sys
sys.stdin = open('input.txt')

def binary_search_iteration(nums, target, start, end):
    global cnt


    while start <= end:
        mid = start + (end - start) // 2            # 가운데 값을 찾고
        if nums[mid] == target:                     # 값을 찾은 경우
            cnt += 1
            return mid                              # 해당 인덱스(mid) 반환
        elif nums[mid] < target:                    # target이 더 크면
            start = mid + 1                         # 왼쪽을 버리자 (start를 mid + 1로 이동)
        else:                                       # target이 더 작으면
            end = mid - 1                           # 오른쪽을 버리자 (end를 mid - 1로 이동)
    return                                          # 못찾은 경우 -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for i in B:
        start = 0
        end = len(A) - 1
        find_val = binary_search_iteration(A, i, start, end)

    print('#{} {}'.format(tc, cnt))






