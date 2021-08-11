import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    ans = 0

    # 0 - 버스 정류장의 시작 지점 / N - 마지막 종점 위치
    chargers = [0] + chargers + [N]
    """
    위의 코드를 메서드로 표현하면 아래 같음
    chargers.insert(0, 0)
    charger.append(N)
    """
    last = 0                    # 가장 마지막에 방문했던 곳의 idx
    for i in range(1, M+2):     # M+2인 이유는 출발점(0)과 도착점(N)의 수를 늘려놓은 2칸을 더해놓고 시작 하기 위함
        if chargers[i] - chargers[i-1] > K:   # 현재 충전기의 위치와 그 전 충전기의 위치의 차이가 K보다 크면 한번의 충전으로 갈 수 없기 때문에
            ans = 0                           # 바로 종료
            break
        if chargers[i] > last + K:  # 만약 충전기의 위치가 마지막으로 버스가 있었던 마지막 위치(last)에서 K만큼 간 곳보다 크다면
            last = chargers[i-1]    # 내가 있었던 바로 직전 충전소로 위치를 옮기고
            ans += 1                # 충전 횟수 증가
    print('#{} {}'.format(tc, ans))