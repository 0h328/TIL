import sys
sys.stdin = open('input.txt')

# thought process:
# 원형 큐 구현해서 문제풀이
# 화덕 크기만큼 front 이동하면, 해당 front 위치 원소 값 // 2
# front 위치 원소 값이 0 되면 deQueue, rear 위치에 새로운 피자 enQueue
# 피자 숫자는 인덱스 활용해서 넣자
# def move():
#     global rear
#     global front
#     # if rear == 0:
#     #     rear = N - 1
#     # else:
#     #     rear -= 1
#     # if front == 0:
#     #     front = N - 1
#     # else:
#     #     front -= 1
#
# def put_pizza():
#     global p_idx
#     p_idx += 1
#     Q.pop(Q[front])
#     Q.append(p[p_idx])


for tc in range(1, int(input())+1):

    N, M = map(int, input().split())        # 화덕크기, 피자개수 인풋값
    p = list(map(int, input().split()))             # 피자들(치즈값) 인풋값
    # p_idx = N - 1                           # 피자 인덱스 값 초기화 (새로 넣기 위함)

    front = 0
    rear = N - 1
    Q = [0] * N                               # 화덕 생성 (큐)
    idx_list = [0] * N                        # 인덱스 리스트 생성
    for i in range(N):                        # 처음에는 화덕 크기만큼 피자 넣음
        Q[i] = p[i]                           # 피자의 치즈값 할당
        idx_list[i] = i+1                     # 피자의 인덱스값 할당

    while len(Q) != 1:
        for i in len(Q):
            Q[i] = Q[i] // 2
            if Q[i] == 0:
                Q.pop(Q[i])
                idx_list.pop(idx_list[i])
                Q.append()
                if


    ans = Q[front]




    # move() 하면서 피자 돌림 (front 와 rear 이용해서 돌림)
    # 매번 빼서 확인할 때 마다 치즈 인풋값 // 2   # 처음부터 계산해도 되는건, 어차피 처음 한바퀴는 아무것도 안 뺄테니 문제x
    # 치즈 인풋값 0 되면, put_pizza()

    # 문제: N - 1 만큼 돌려야 치즈가 줄어드는데, pop을 해버리면 회전 횟수가 줄어들어서 문제가 되는게 아닐까?
    # 해답: 기준이 몇 칸을 가는게 아니라, 회전 수 니까, 상관 없다. 화덕크기가 줄어들더라도 회전 횟수는 동일하니까

    # 애초에 Q 에 초기 피자들을 집어넣고,