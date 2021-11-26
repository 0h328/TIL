import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    cnt = int(input())                          # 빌딩 수
    buildings = list(map(int, input().split())) # 빌딩 목록
    ans = 0                                     # 조망권 확보된 집

    for i in range(cnt):
        cur_height = buildings[i]               # 현재 빌딩의 높이
        if not buildings[i]:                    # 건물이 없는 곳(0인 곳)은 넘어가고 (양 끝 2개씩은 빌딩 없음)
            continue
        else:                                   # 건물이 있는 곳은
            max_height = 0                      # 건물 최대 높이를 초기화
            for side in range(4):
                idx = [-2, -1, 1, 2]            # 빌딩 양 옆에 접근하기 위한 idx
                if buildings[i+idx[side]] > max_height: # max_height보다 큰 건물이 있다면
                    max_height = buildings[i+idx[side]] # 최대 높이 갱신

            if cur_height > max_height:         # 현재 건물 높이가 최대 건물 높이보다 높은 경우는
                ans += cur_height - max_height  # 그 차이만큼 조망권 값에 누적
    print('#{} {}'.format(tc, ans))