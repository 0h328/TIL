import sys
sys.stdin = open('input.txt')

for _ in range(1):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    # for i in range(N):
    #     st = road[2*i]
    #     ed = road[2*i+1]

    ch1 = [0] * 100
    ch2 = [0] * 100

    for i in range(N):
        if ch1[road[2*i]] == 0:
            ch1[road[2*i]] = road[2*i+1]
        else:
            ch2[road[2*i]] = road[2*i+1]

    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1

    adj_list = [[] ]
