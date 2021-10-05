import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    result = 0
    for i in range(M):
        can_go = []
        for j in range(N):
            if truck[i] >= weight[j] and weight[j] != 0:
                can_go.append(weight[j])
        if len(can_go) != 0:
            result += max(can_go)
            for j in range(N):
                if weight[j] == max(can_go):
                    weight[j] = 0
                    break

    print("#{} {}".format(tc, result))