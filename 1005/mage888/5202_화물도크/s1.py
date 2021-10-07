import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = sorted((list(map(int, input().split())) for _ in range(N)), key=lambda e: e[1]) # 종료시간 기준 정렬

    truck = 0
    var = 0                     # 이전 종료시간과 다음 시작시간을 비교해주기 위한 변수
    for i in range(N):
        if arr[i][0] >= var:    # 시작시간이 0, 이전 종료시간보다 크다면
            truck += 1          # 화물차 1대가 이용 가능
            var = arr[i][1]     # 종료시간을 업데이트

    print('#{} {}'.format(tc, truck))