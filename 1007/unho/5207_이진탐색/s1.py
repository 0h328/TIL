import sys
sys.stdin = open('input.txt')


def binary_search(low, high, target, direction):        # direction / 0 - start / 1 - left / 2- right
    global answer

    if low > high:
        return

    mid = (low + high) // 2

    if n_li[mid] < target and (not direction or direction == 1):
        binary_search(mid+1, high, target, 2)

    elif n_li[mid] > target and (not direction or direction == 2):
        binary_search(low, mid-1, target, 1)
    
    elif n_li[mid] == target:
        answer += 1
        return
    

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    n_li = sorted(list(map(int, input().split())))
    m_li = set(map(int, input().split()))

    answer = 0

    for target in m_li:
        binary_search(0, N-1, target, 0)

    print('#{} {}'.format(tc, answer))