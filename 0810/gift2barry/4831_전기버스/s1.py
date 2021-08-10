import sys
sys.stdin = open('input.txt')
# 문제 요약:
# 버스는 0 에서 출발
# N = 최종 목표 정류장
# K = 한번 충전으로 이동 가능한 정류장 수
# M = 설치된 충전기 개수
# ans = 최소 충전 횟수

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

def init():
    for _ in T:
        # 노선 개수
        T = int(input()) - 1
        K, N, M = map(int, input().split())
        gas = list(map(int, input().split()))

        # 카운트 배열을 만들어서, 만약 1 이 있으면 거기가 가스 스탠드 위치
        gas_stand = [0 for _ in range(N)]
        for i in gas:
            gas_stand[i] += 1

        #최대 반복 횟수는 주유소의 최대값
        for i in range(M):


def goOrNo():
    # 이동시:
    # K - 이동거리, N - 이동거리
    # 비이동시:
    # K 초기화, M - 1
    #


init()


테스트케이스 길이만큼 루프
