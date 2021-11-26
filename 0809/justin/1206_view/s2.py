def solve(length, buildings):
    global ans
    i = 2     # 가운데를 기준으로 양 옆 네 곳을 체크하기 위한 idx
    j = 0
    while i != length:             # 테스크 케이스의 길이를 넘지 않는 선에서(모든 세대 확인)
        if (buildings[i-2] < buildings[i]) and (buildings[i-1] < buildings[i]) and (buildings[i+1] < buildings[i]) and (buildings[i+2] < buildings[i]): # 조망권이 확보됐다면
            buildings[i] -= 1      # 한 세대를 줄여서 다시 확인
            ans += 1               # 한 세대의 조망권 확보 count
            j += 1                 # 7번째 줄에서 줄인 세대를 다음 조망권 확인할 때 쓰기 위해 원상복구하기 위한 값
        else:                      # 조망권이 확보되지 않았고
            if j:                  # 만약 원상복구 할게 있다면
                buildings[i] += j  # 다시 원상복구
                j = 0              # 0으로 초기화
            i += 1                 # 원상복구 할 것이 없다면 다음 building의 조망권 확인
    return ans

import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    L = int(input())                             # 테스트 케이스 길이
    buildings = list(map(int, input().split()))  # 빌딩 목록
    ans = 0                                      # 조망권이 확보된 세대 수
    solve(L, buildings)
    print('#{} {}'.format(tc, ans))