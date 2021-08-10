import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K: 한번 충전으로 이동할 수 있는 최대 정류장 수
    # N: 타겟 정류장
    # M: 충전기 설치된 정류장 수
    K, N, M = map(int, input().split())
    gas_stations = tuple(map(int, input().split()))
    charged = K
    ans = 0
    gas_idx = 0

    for i in range(1, N+1):
        charged -= 1
        if gas_stations[gas_idx] == i:    # 현 위치가 gas station일 때
            if gas_idx == len(gas_stations) - 1:    # 마지막 gas station일 경우
                if K < N - i:   # 1회 충전 최대 거리가 남은 거리보다 짧은 경우
                    ans = 0
                    break
                elif charged >= N - i: # 현재 충전량으로 다 갈 수 있는 경우
                    break
                elif K >= N - i:    # 현재 충전량으로는 부족하지만 다시 충전하면 갈 수 있는 경우
                    ans += 1
                    break
            else:   # 마지막 gas 스테이션 아닌 경우
                if charged < gas_stations[gas_idx+1] - i:   # 이번 충전소에서 충전해야 하는 경우
                    charged = K
                    ans += 1
                gas_idx += 1
        else:   # 현 위치가 gas station 아닐 때
            if charged >= N - i:    # 충전량으로 남은 거리 다 갈 수 있는 경우
                break
            else:
                if charged < gas_stations[0] - i or charged == 0:
                    ans = 0
                    break

    print('#{} {}'.format(tc, ans))

