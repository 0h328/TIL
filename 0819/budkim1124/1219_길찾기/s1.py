import sys
sys.stdin = open('input.txt')

# 인덱스를 노드 // 값을 연결되는 값으로 배열을 지정한다.
# range(0, len(road), 2)

# 어떻게 저장할 것인가?
# ch1 , ch2
# ch1 = [0] * 100
# ch2 = [0] * 100
# ch1에 차있는지 확인한 후 ch2에 넣어라

for _ in range(1):
    tc, N = map(int, input().split())
    road = list(map(int,input().split()))  # 공백 단위로 준다면 .split()을 쓴다.

    # 1. 홀짝 방법
    # 2. 2 step

    # 3. 2*? # 선택
    # for i in range(N):
    #     st = road[2*i]
    #     ed = road[2*i+1]

    ##########################
    # 저장 방법
    # 1. ch1, ch2 : 최대 길이의 개수는 2개만 들어온다고 했기 때문에 2개만 지정해도 됨
    ch1 = [0] * 100
    ch2 = [0] * 100

    for i in range(N):
        if ch1[road[2*i]] == 0: # ch1부터 채워나갈건데 0인지 아닌지 판단해야함
            # 2*i는 시작점을 넣는다.
            ch1[road[2*i]] = road[2*i+1]
        else:
            ch2[road[2*i]] = road[2*i+1]

    # 2. 인접 행렬 방식
    adj_arr = [[0] * 100 for _ in range(100)] # 100*100 이차원 배열 생성
    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1
        # 무 방향성이면 뒤집어서 1을 똑같이 지정해야하지만 지금은 방향성이 있기 때문에 하지 않는다.

    # 3. 인접 리스트 방식
    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2*i]].append(road[2*i+1])