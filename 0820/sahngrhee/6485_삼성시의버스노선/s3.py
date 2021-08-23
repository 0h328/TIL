import sys
sys.stdin = open('input.txt')

# 3. 미리 계산2
T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 버스 노선 수

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B+1):
            bus_stop[j] += 1

    P = int(input())
    print('#{}'.format(test_case), end=' ')
    for i in range(P):
        C = int(input())  # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()  # 다음 test_case를 위해서 꼭 주의!