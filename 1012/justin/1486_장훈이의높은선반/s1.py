def solve(k, cur_sum):
    global ans
    if cur_sum < B:                 # 직원 키의 합이 탑 보다는 높아야 함 -> 작으면 가지치기
        return
    if cur_sum < ans:               # 최솟값 갱신
        ans = cur_sum
    if k == N:                      # 모든 직원을 체크했다면 종료
        return
    solve(k+1, cur_sum-heights[k])  # 그 다음 점원 확인
    solve(k+1, cur_sum)             # 원상복구

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())              # N: 점원 수, B: 탑의 높이 (높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑 찾기)
    heights = list(map(int, input().split()))     # 점원들의 키
    ans = 987654321                               # 최솟값 초기화
    heights.sort(reverse=True)                    # 내림차순 정렬 (B 이상이면서 최소가 되는 탑의 높이를 찾기 위함)
    solve(0, sum(heights))                        # k: 직원 선택 / cur_sum: 직원들의 키 합
    result = ans - B                              # 높이가 B 이상이면서 최솟값 - B
    print('#{} {}'.format(tc, result))