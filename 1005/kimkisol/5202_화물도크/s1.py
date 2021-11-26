import sys

sys.stdin = open('input.txt')

'''
1. 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
2. 최대 몇 대의 화물차가 이용할 수 있는지 출력
'''
T = int(input())

#  가장 무거운거를 가장 적재용량이 적은것부터 비교해서 운반 가능할 경우 넣는 방법
for t in range(1, T + 1):
    N = int(input())  # N: 신청서 수
    work_times = [[0, 0] for _ in range(N)]

    for i in range(N):
        work_times[i][1], work_times[i][0] = map(int, input().split())  # 신청서의 (e, s)
    work_times.sort()  # 종료시간 기준 오름차순 정렬
    e = work_times[0][0]  # 가장 종료시간이 이른 0번째거를 e로 설정
    cnt = 1  # 0번째거는 이미 작업됐으므로 1로 초기화


    for i in range(1, N): # 1번째~마지막
        if work_times[i][1] >= e:  # 해당 신청서 시작시간이 종료시간 보다 같거나 클때
            e = work_times[i][0]  # 종료시간은 해당 신청서 종료시간으로 업데이트
            cnt += 1  # 작업 처리 개수 +1

    print('#{} {}'.format(t, cnt))