import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container = sorted(container, reverse=True)
    truck = sorted(truck, reverse=True)
    idx = 0
    jdx = 0
    result = 0

    while idx < len(truck) and jdx < len(container):
        if truck[idx] >= container[jdx]:
            result += container[jdx]

            idx += 1
            jdx += 1
        else:
            jdx += 1
    print('#{} {}'.format(tc, result))

