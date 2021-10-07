# 문제 풀이 시간 : 2시간
# 해결? : yes 하지만 혼자 힘으로 하지 못했다. -> 정렬까지는 혼자 했는데 비교를 어떻게 할 지 고민을 많이 했다 ㅜㅜ 궁금해서 구글링 해 봄

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trucks = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(i, N):
            if trucks[i][1] > trucks[j][1]:
                trucks[i], trucks[j] = trucks[j], trucks[i]
    cnt = 1
    compare = trucks.pop(0)

    while trucks:                       # 트럭이 있는 동안
        if trucks[0][0] < compare[1]:   # 트럭 내의 첫번째 값(시작할 시간)과 비교할 값의 두번째 값(끝난 시간)
            trucks.pop(0)
        else:
            cnt += 1
            compare = trucks.pop(0)

    # print(trucks)
    print('#{} {}'.format(tc, cnt))