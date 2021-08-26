import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    W = []
    for num, pizza in enumerate(list(map(int, input().split())), 1):
        W.append([num, pizza])

    Q = W[:N]
    R = W[N:]

    while len(Q) > 1:
        Q[0][1] //= 2
        if Q[0][1] == 0:
            Q.pop(0)
            if R:
                Q.append(R.pop(0))
        else:
            Q.append(Q.pop(0))

    print('#{} {}'.format(test_case, Q[0][0]))










