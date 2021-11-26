import sys
sys.stdin = open('input.txt')
# 문제 요약:
# 버스는 0 에서 출발
# N = 최종 목표 정류장
# K = 한번 충전으로 이동 가능한 정류장 수
# M = 설치된 충전기 개수
# ans = 최소 충전 횟수

# thought process: 6분 42초
# 0 부터 N 번 안에서
# K 만큼 빼주고, 그 위치에 충전소 있는지 없는지 확인
# 있으면 또 이동, 없으면 한칸 뒤로갔다가 다시 충전소 확인
# 있으면 K만큼 이동, 없으면 똑같은거 반복
# 충전소에 위치할 떄 마다 cnt 하나씩 올리고
# N 이상 위치에 도달하면 루프 끝내고 cnt 반환

# 문제해결: 2시간 46분

def counter(stations):
    global cnt
    global position

    for i in range(stations):      # 최대 충전기 개수만큼 반복

        if station_nums[-1] != station_nums[i]:             # 다음 충전소가 존재할 때,
            if station_nums[i+1] - station_nums[i] > go:    # 충전소 사이 거리가 충전이동거리보다 멀 경우,
                return 0                                    # 도달 불가
            if station_nums[0] > go                         # 처음위치에서 충전소에 도달 못할때
                return 0                                    # 도달 불가

        else:                                               # 다음 충전소가 없을 때,
            if N - station_nums[-1] > go:                   # 마지막 충전소에서 목적지까지가 충전이동거리보다 멀 경우,
                return 0                                    # 도달 불가

        position += go             # 처음 go 만큼 이동

        if position >= N:           # 현위치가 목표지점이거나 더 멀리 가 있으면
            return cnt              # 함수 종료하고 cnt 반환

        while position >= station_nums[i]:  # 충전소에 도달할떄 까지 반복
            if position in station_nums:    # 어디든 충전소 위치에 있으면 루프 빠져나옴
                break
            elif position > station_nums[i]:    # 현위치가 충전소보다 멀리가있으면
                position -= 1                   # 충전소 만날때 까지 한칸씩 뒤로
        cnt += 1                            # 충전소 만나면 충전

for tc in range(1, int(input())+1):

    go, N, station = map(int, input().split())  # 이동가능거리, 총 거리, 충전소 개수 변수에 할당

    station_nums = list(map(int, input().split()))  # 충전기 설치된 곳 위치 리스트 변수에 할당
    position = 0                    # 현위치 변수
    cnt = 0                         # 충전 횟수 카운터
    print('#{} {}'.format(tc, counter(station)))


# 패작 1
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

# thought process 2:
# if 매번 이동 가능 거리가 충전소 간에 거리보다 짧으면:
#     0 반환
# else 이동거리가 총 길이보다 작을때 루프:

# 패작 2
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

