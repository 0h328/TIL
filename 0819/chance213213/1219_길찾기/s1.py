import sys
sys.stdin = open('input.txt')



for tc in range(10):
    N, M = map(int, input().split())

    road = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    for i in range(M):
        adj_list[road[2*i]].append(road[2*i+1])



    # road_arr1 =[0] * 100
    # road_arr2 = [0] * 100
    # for idx in range(0, len(road), 2):
    #     print(road[idx], road[idx+1])
    #     if road_arr1[road[idx]] == 0:
    #         road_arr1[road[idx]] += road[idx+1]
    #     else:
    #         road_arr2[road[idx]] += road[idx+1]

    visited = [0] * 100
    ans = 0

    stack = [0]

    while stack:
        curr = stack.pop()

        #방문 X
        if curr == 99:
            ans = 1
            break
        #방문 O
        if visited[curr]:
            continue
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(w)

    print('#{} {}'.format(N, ans))
    #
    # ch1 = [0] * 100
    # ch2 = [0] * 100
    #
    # for i in range(N):
    #     if ch1[road[2*i]] == 0:
    #         ch1[road[2*i]] = road[2*i+1]
    #     else:
    #         ch2[road[2*i]] = road[2*i+1]
    #
    # adj_arr = [[0]*100 for _ in range(100)]
    # for i in range(N):
    #     adj_arr[road[2*i]][road[2*i+1]] = 1

