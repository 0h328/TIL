import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    truck.sort()
    total = 0
    # 각 트럭이 운반할 수 있는 최대의 화물을 운반해야 함
    # sort를 통해 truck을 작은순으로 정렬하고 그 상태에서 최대 옮길 수 있는 화물
    for i in range(len(truck)):
        move = 0
        for w in range(len(weight)):
            temp = 0
            if truck[i] >= weight[w]:
                temp = weight[w]
                if temp > move:
                        move = weight[w]
        total += move
        if move: # move가 0이면 옮길 수 없는 화물이 없는 것이므로 패스, 0 아니면 weight에서 옮긴 화물 삭제
            weight.remove(move)

    print('#{} {}'.format(t, total))
