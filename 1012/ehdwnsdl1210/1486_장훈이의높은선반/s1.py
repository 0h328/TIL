'''
서점에는 높이가 B인 선반 / N명의 점원들
각 점원의 키는 Hi
점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.
탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.
탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데 탑의 높이가 높을수록 더 위험하므로
높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.

만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것을 출력!
'''

import sys
sys.stdin = open('input.txt')

def DFS(n):
    global result
    global min_value

    # if n == N:
    #     if result >= B:
    #         if result - B <= min_value:
    #             min_value = result - B
    #             return
    #     else:
    #         return

    if result >= B:
        if result - B <= min_value:
            min_value = result - B
            return
        else:
            return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            result += H[i]
            if result - B > min_value:
                continue
            DFS(n+1)
            visited[i] = 0
            result -= H[i]

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())        # 점원수 / B 장훈이 기준 높이
    H = list(map(int, input().split()))     # 점원수 만큼 각각의 높이
    visited = [0] * N
    result = 0
    min_value = 987654321

    DFS(0)

    print('#{} {}'.format(tc, min_value))

'''
#1 1
#2 4
#3 27

#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0
'''