from collections import deque
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())            # N: 점원 수, B: 탑의 높이 (높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑 찾기)
    heights = list(map(int, input().split()))   # 직원의 키

    Q = deque()
    Q.append((0, 0))
    ans = 987654321

    while Q:
        k, s = Q.popleft()
        if B <= s < ans:
            ans = s
            if s == B:
                break

        if k == N:                              # 점원 다 선택한 경우 넘어가자
            continue
        if s + heights[k] < ans:                # 최소이면
            Q.append((k+1, s+heights[k]))       # 다음 점원 확인
        Q.append((k+1, s))                      # dfs의 원상 복구와 같은 로직 (그냥 다음으로)

    result = ans - B
    print('#{} {}'.format(tc, result))