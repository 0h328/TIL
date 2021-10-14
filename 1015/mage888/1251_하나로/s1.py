import sys
sys.stdin = open('input.txt')

def prim():
    for _ in range(N):
        min_idx = -1
        min_val = 1e13
        for i in range(N):
            if not v[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]
        v[min_idx] = 1

        for i in range(N):
            if not v[i]:
                cost = ((X[min_idx]-X[i])**2 + (Y[min_idx]-Y[i])**2) * E
                if cost < key[i]:
                    key[i] = cost

    return round(sum(key))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    v = [0] * N
    key = [1e13] * N
    key[0] = 0

    print('#{} {}'.format(tc, prim()))


