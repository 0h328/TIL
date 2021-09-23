def heap_push(value):
    global heap_count

    heap_count += 1
    heap[heap_count] = value
    child = heap_count
    parent = child // 2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    N = len(nums)
    heap = [0] * (N+1)
    heap_count = 0
    ans = 0

    for i in range(n):
        heap_push(nums[i])

    while n > 0:
        n //= 2
        ans += heap[n]

    print('#{} {}'.format(test_case, ans))