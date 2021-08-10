import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):   # 입력받는부분
    K, N, M = map(int, input().split())
    number = list(map(int, input().split()))
    cnt = [0] * (N + 1 + K) # 충전소가 있는 부분을 넣기 위함인데 마지막 갯수에서 정류장 넘어 공간까지 탐색할 경우를 대비
    charge_cnt = 0  # 충전 횟수 카운트

    for num in number:  # 충전소 있는 위치 기록
        cnt[num] += 1
    i = 0
    while i < N:    # 위치가 종점 N에 도달하기 전까지 확인
        for k in range(K, 0, -1):   # 가장 멀리 갈 수 있는 충전소의 위치를 확인하기 위함
            if i + k >= N:  # 종점 N을 넘어버리면 게임끝
                i += k  # 그럼에도 k를 더해주는것은 while문을 끝내기 위함!!!!@!@
                print('#{} {}'.format(test_case, charge_cnt))
                break   # for문을 탈출

            elif cnt[i + k] == 1:   # 충전기를 찾으면 충전기 위치로 이동 및 횟수 추가
                i += k
                charge_cnt += 1
                break

        else:   # for-else구문을 통해 충전기를 찾지 못한 경우 출력을 시행하는 모습
            charge_cnt = 0
            print('#{} {}'.format(test_case, charge_cnt))
            break
