import sys
sys.stdin = open('input.txt')

# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    load = list(map(int, input().split()))        # N개의 화물이 무게
    capacity = list(map(int, input().split()))    # M개 트럭의 적재용량
    load.sort(reverse=True)
    capacity.sort(reverse=True)
    weight = 0
    i, j = 0, 0  # load의 index i, capacity의 index j
    times = 0

    while times < min(N, M):
        if load[i] > capacity[j]:
            i += 1
        else:
            weight += load[i]
            i += 1
            j += 1
        times += 1

    print('#{} {}'.format(tc, weight))

