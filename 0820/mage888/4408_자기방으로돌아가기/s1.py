def div(num):
    return (int(num)+1) // 2


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    s = [list(map(div, input().split())) for _ in range(N)]
    # 사용자 정의 함수로 변경 가능
    # s = [list(map(int, input().split())) for _ in range(N)]

    road = [0] * 201

    # 돌아갈 방의 번호가 더 크다는 것에 주의
    # for _ in range(N):
    #     now, back = map(int, input().split())

    for i in range(N):
        if s[i][0] > s[i][1]:
            s[i][0], s[i][1] = s[i][1], s[i][0]

        for j in range(s[i][0], s[i][1] + 1):
            road[j] += 1

    print('#{} {}'.format(tc, max(road)))