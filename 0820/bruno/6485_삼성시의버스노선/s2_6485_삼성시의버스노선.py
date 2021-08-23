import sys
sys.stdin = open('input.txt')
# 2. 정류장 미리 계산

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    start = [0] * 5001  # 출발 정류장 표시
    end = [0] * 5001    # 도착 정류장 표시
    bus_stop = [0] * 5001   # 계산한 버스 표시

    for i in range(N):
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1

    for i in range(len(bus_stop)-1):
        bus_stop[i+1] = bus_stop[i] - end[i] + start[i+1]

    P = int(input())
    print('#{}'.format(tc), end=' ')
    for i in range(P):
        C = int(input())    # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()
