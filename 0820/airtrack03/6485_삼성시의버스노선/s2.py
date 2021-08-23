'''
P개의 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지?
=> 각 정류장에서 이전 정류장에서 계산된 값에 해당 정류장에서 새롭게 출발하는 버스를 더하고 해당 정류장에 도착하는 버스를 빼준다!
=> 잘 이해가 안됨....
'''

import sys

sys.stdin = open('input.txt')
T = int(input())

# 방법 1. 모든 노선 체크

# def bus_count(bus_stop):
#     cnt = 0
#
#     for i in range(N):
#         if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
#             cnt += 1
#
#     return cnt
#
# for tc in range(1, T+1):
#     N = int(input())    # 버스 노선 개수
#     bus_route = [list(map(int, input().split())) for _ in range(N)]     # 버스 노선 저장 리스트
#     P = int(input())    # P 개의 정류장
#     ans = []
#
#     for i in range(P):
#         C = int(input())
#         ans.append(bus_count(C))
#
#     print('#{} {}'.format(tc, ' '.join(map(str, ans))))

# 방법 2. 정류장 미리 계산

for tc in range(1, T+1):
    N = int(input())

    start = [0] * 5001      # 출발 정류장
    end = [0] * 5001        # 도착 정류장
    bus_stop = [0] * 5001   # 계산한 버스 수

    for i in range(N):
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1
    # 버스 계산
    for i in range(len(bus_stop)-1):
        bus_stop[i+1] = bus_stop[i] + start[i+1] - end[i]

    P = int(input())
    print('#{}'.format(tc), end=' ')
    for i in range(P):
        C = int(input())    # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()