import sys
sys.stdin = open("input.txt")

def binary(nums, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    n_list = list(map(int,input().split()))
    m_list = list(map(int,input().split()))
    cnt = 0

    for num in n_list:
        start = 0
        end = len(m_list) - 1
        result = binary(m_list, num, start, end)
        if result == 1:
            cnt += 1

    print("#{} {}".format(t+1, cnt))

