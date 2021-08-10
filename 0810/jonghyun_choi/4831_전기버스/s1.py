import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    K, N, M = map(int,input().split())
    battery_number = list(map(int,input().split()))

    busstop_number = [i for i in range(N+1)]

    cnt = 0
    i = 0
    while i < N:
        con_cnt = 0
        for j in range(K,0,-1):
            if con_cnt != 0:
                continue
            if i+j >= N:
                con_cnt += 1
                break
            if i+j in battery_number:
                cnt += 1
                dis = j
                con_cnt += 1
        if con_cnt == 0:
            cnt = 0
            break
        i = i + dis
    print('#{} {}'.format(case+1,cnt))





