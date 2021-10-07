# 리뷰하면서 느낀 점 : 정렬할 생각을 못했네,,,?

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
            if truck[i] >= weight[j] and weight[j] != 0: # 트럭보다 가벼운 무게의 컨테이너만 append
                can_go.append(weight[j])
        if len(can_go) != 0:
            result += max(can_go) # 가장 큰 값을 result에 더하기
            for j in range(N):
                if weight[j] == max(can_go): # 무게가 가장 무거운 짐을
                    weight[j] = 0            # 0으로 만든다!
                    break

    print("#{} {}".format(tc, result))