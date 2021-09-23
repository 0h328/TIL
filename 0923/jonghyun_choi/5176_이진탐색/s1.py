import sys
sys.stdin = open('input.txt')


def push(value):
    global cnt
    if value <= N:
        push(value * 2)
        heap[value] = cnt
        cnt += 1
        push(value * 2 + 1)

T = int(input())

for case in range(T):
    N = int(input())
    nums = list(range(N + 1))
    cnt = 1
    l = len(nums)
    heap = [0] * l
    push(1)
    print('#{} {} {}'.format(case + 1, heap[1], heap[N//2]))




