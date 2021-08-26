import sys
sys.stdin = open('input.txt')

T = int(input())


for case in range(T):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pos = [[i+1,cheese[i]] for i in range(M)]
    fire = [-1] * N
    i = 1
    res = []
    for idx in range(N):
        fire[idx] = pos.pop(0)

    while True:
        if fire == [[-1, -1] for _ in range(N)]:
            break
        if fire[0][1] == 0:
            res.append(fire.pop(0)[0])
            if pos:
                fire.append(pos.pop(0))
                fire[-1][1] //= 2
            else:
                fire.append([-1,-1])

        else:
            if fire[0][1] != -1:
                fire[0][1] //= 2
            fire.append(fire.pop(0))
    print('#{} {}'.format(case + 1, res[-1]))









