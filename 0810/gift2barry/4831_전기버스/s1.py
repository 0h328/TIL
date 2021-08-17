import sys
sys.stdin = open('input.txt')
# 문제 요약:
# 버스는 0 에서 출발
# N = 최종 목표 정류장
# K = 한번 충전으로 이동 가능한 정류장 수
# M = 설치된 충전기 개수
# ans = 최소 충전 횟수

# thought process:
#
# 현재위치 알람용 변수 L 하나 생성
#
# if (충전소 개수 * 한번충전으로 이동 가능 거리) < 총 거리:
#     0 반환
#
# else:
#     세칸 갔다가 충전소 있으면 이동거리++ 충전 횟수 ++,
#     없으면 한칸씩 뒤로가면서 현재위치 -- 찾으면 충전 횟수 ++,
#
# else 를 무한반복 하다가 L 이 최종위치 도달 하면 바로 루프 종료후
#     누적된 충전횟수 반환
#
# 문제: 최종위치를 넘어버리면?
# 문제2: 엣지케이스: 첫 루프때 어떻게 접근할건가?

thought process 2:
if 매번 이동 가능 거리가 충전소 간에 거리보다 짧으면:
    0 반환
else 이동거리가 총 길이보다 작을때 루프:
    








# thought process:
# 첫번째 충전소까지 이동,
# 이동시, 이동 거리만큼 K 소비
# 다음 충전소까지 거리와 K 잔량 비교,
# 다음 충전소까지 이동 가능하면 충전 안하고 다음 까지 이동,
#     불가능하면 충전하고(M - 1), K 초기화하고 다음 까지 이동
# 다음 충전소까지 거리와 K 잔량 비교,
# 다음 충전소까지 이동 가능한면 충전 안하고 다음 까지 이동,
# (이동시, N - 이동거리)
# 무한반복
#
# 남은 K 안에 M 에 도달 가능하면, 축적된 ans 반환

# def init():
#     for _ in T:
#         # 노선 개수
#         T = int(input()) - 1
#         K, N, M = map(int, input().split())
#         gas = list(map(int, input().split()))
#
#         # 카운트 배열을 만들어서, 만약 1 이 있으면 거기가 가스 스탠드 위치
#         gas_stand = [0 for _ in range(N)]
#         for i in gas:
#             gas_stand[i] += 1
#
#         #최대 반복 횟수는 주유소의 최대값
#         for i in range(M):
#
#
# def goOrNo():
#     # 이동시:
#     # K - 이동거리, N - 이동거리
#     # 비이동시:
#     # K 초기화, M - 1
#     #
#
#
# init()

