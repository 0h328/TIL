import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    Truck = list(map(int, input().split()))

    sorted_w = sorted(W, reverse = True)
    sorted_truck = sorted(Truck, reverse = True)


    res = 0
    idx = 0
    for i in range(len(sorted_w)):
        if idx == len(sorted_truck):
            break
        if sorted_truck[idx] >= sorted_w[i]:
            res += sorted_w[i]
            idx += 1
    print('#{} {}'.format(case + 1, res))
