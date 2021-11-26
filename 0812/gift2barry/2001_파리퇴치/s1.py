import sys
sys.stdin = open('input.txt')

# 소요시간 1시간 20분42초

# thought process:
# 좌측상단을 시작점으로 파리채 크기만큼 하나하나 합을 구해본다
# row 와 column의 마지막 라인은 확인 할 필요x
# 가장 큰 값을 초기에 정하고, 큰 값을 갱신해나간다
# 전체를 확인 하면 최종 큰 값을 리턴!


T = int(input())

for tc in range(1, T+1):

    length, parichae = map(int, input().split())
    killing_floor = [list(map(int, input().split())) for _ in range(length)]

    max_kill = 0                    #최대 킬을 저장

    for r in range(length-parichae +1):         # row 위치 지정 / +1 이유: length-parichae 의 인덱스값 만큼 루프 하려면, range(인덱스값 + 1) 을 해야 인덱스값 만큼 루프 한다.
        big_kills = 0                           # 하나의 row 에서 가장 큰 킬 값 초기화
        for c in range(length-parichae +1):     # column 위치 지정
            kills = 0                           # 한번 내리칠때 마다의 킬 값 초기화
            for hit_c in range(parichae):       # 내려친 위치의 column 위치
                 for hit_r in range(parichae):  # 내려친 위치의 row 위치
                     kills += killing_floor[r+hit_c][c+hit_r]   # 내려친 위치의 특정 원소값들을 하나하나 kills 에 더해나가서, 한번 내리쳤을때 총 킬값 구함
            if kills > big_kills:               # 한번 내리쳤을때 총 킬값이 현제의 row 내에서 가장 크면
                big_kills = kills               # 큰 킬 값 업데이트
        if big_kills > max_kill:                # 하나의 row 킬 계산이 끝날때 마다, max_kill의 현재값보다 크면
            max_kill = big_kills                # max_kill 값 업데이트
    print('#{} {}'.format(tc, max_kill))


# 패작 1
    # for r in range(length - parichae):
    #     kills = 0
    #     for c in range(length - parichae):
    #             kills += sum(killing_floor[c][r:r+parichae])
    #     if kills > max_kill:
    #         max_kill = kills
    # print(max_kill)


