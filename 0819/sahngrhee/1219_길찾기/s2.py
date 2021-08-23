import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2 * i]].append(road[2 * i + 1])

    visited = [0] * 100
    ans = 0

    stack = [0]

    while stack:
        curr = stack.pop()

        if curr == 99:
            ans = 1
            break
        #방문하지 않았으면

        #방문을 했으면 건너가~
        if visited[curr]: continue
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(w)

    print('#{} {}'.format(tc, ans))

    # 1. 홀짝
    # 2. 2step

    # 3. 2*?
    # for i in range(N):
    #     st = road[2*i]
    #     ed = road[2*i+1]

    ################################
    # 저장 방법
    # 1. ch1, ch2
    # ch1 = [0] * 100
    # ch2 = [0] * 100
    #
    # for i in range(N):
    #     if ch1[road[2*i]] == 0:
    #         ch1[road[2*i]] = road[2*i+1]
    #     else:
    #         ch2[road[2*i]] = road[2*i+1]
    #
    # 2. 인접행렬 방식
    # adj_arr = [[0] * 100 for _ in range(100)]
    # for i in range(N):
    #     adj_arr[road[2*i]][road[2*i+1]] = 1
    #
    # 3. 인접리스트 방식
    # adj_list = [[] for _ in range(100)]
    # for i in range(N):
    #     adj_list[road[2*i]].append(road[2*i+1])
