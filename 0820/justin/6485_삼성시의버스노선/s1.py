import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):       # 해당 정류장에 지나는 버스의 대수 누적
            bus_stop[j] += 1

    P = int(input())                  # 확인하고 싶은 버스 정류장의 수
    print('#{}'.format(tc), end=' ')
    for i in range(P):
        C = int(input())              # 확인하고 싶은 정류장의 번호
        print(bus_stop[C], end=' ')   # 해당 위치(인덱스) 버스 정류장에 몇개의 버스 노선이 지나는지 확인
    print()