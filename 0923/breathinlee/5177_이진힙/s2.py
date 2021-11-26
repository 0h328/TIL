import sys
sys.stdin = open('input.txt')

def heap_push(value):
    global heap_count
    heap_count += 1
    heap[heap_count] = value
    child = heap_count
    parent = child // 2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    heap = [0] * (N + 1)
    heap_count = 0
    ans = 0

    for i in range(N):
        heap_push(temp[i])

    while N:
        N //= 2
        ans += heap[N]

    print('#{} {}'.format(tc, ans))

