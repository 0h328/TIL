import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    fire = [[0, 0] for _ in range(N)]
    idx, state, cnt = 0, 0, 0

    while cnt < M-1:
        if fire[idx][0] > 0:
            fire[idx][0] //= 2
        if fire[idx][0] == 0:
            if fire[idx][1] == 0:
                fire[idx] = [arr[state], state+1]
                state += 1
            else:
                cnt += 1
                if state < M:
                    fire[idx] = [arr[state], state+1]
                    state += 1
                else:
                    fire[idx][0] = -1
        idx = (idx+1) % N

    for i in range(M):
        if fire[i][0] > 0:
            print('#{} {}'.format(test+1, fire[i][1]))
            break