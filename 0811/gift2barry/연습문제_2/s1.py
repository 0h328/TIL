import sys
sys.stdin = open('input.txt')








## 대 패작 1
# thought process:
# 1.원소 하나씩 접근,
# 2.상하좌우와 현재위치의 값들의 합을 변수에 저장
# 1 과 2를 루프 but,
# -2차원 배열의 벽을 벗어나면 다음 column으로 이동 후 재개
# -루프 횟수가 전체 원소 개수에 도달하면 끝

# T = int(input())
#
# for tc in range(T):
#     #인풋값들
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     #총 합 변수 초기화
#     ans = 0
#
#     # 현재 위치 초기화
#     r = 0
#     c = 0
#
#     #    상  하  좌 우
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     for i in range(N):          # 1차원 배열의 길이만큼 루프
#         temp = 0                # 상하좌우 값 더해나갈 변수
#         for j in range(N):
#
#             for drc in range(4):      #상 하 좌 우 의 원소값을 구하기위해 4번 루프
#
#                 # 루프가 돌 때 마다 원소의 위치 바꿔준다
#                 nr = r + dr[drc]  # dr값 대로 상,하,좌,우 row 위치
#                 nc = c + dc[drc]  # dc값 대로 상,하,좌,우 column 위치
#
#                 # 2차원 배열의 벽 안으로 들어오는 경우
#                 if (0 <= r < N) and (0 <= c < N):
#                     temp += data[nr][nc]
#                     r += 1              #현재 위치 가로 한칸 이동
#
#                 # 벽 밖으로 나가는 경우는 다음 배열로 이동
#                 if r < 0 or r >= N or c < 0 or c >= N:
#                     r = 0               # row 값 0 으로 초기화
#                     c += 1              # 현재 위치 세로 한칸 이동
#
#                                     # 현재위치: data[r][c]
#             ans += temp + data[r][c]    # 현재위치 원소값과 해당 위치의 상하좌우값의 총합을 더한다
#
#     print(ans)

