# 먼소린지
# 노선 N / 정류장 P
"""
N = 5       P = 5
13          1       2대
25          2       4대
78          3       4대
19          4       2대
23          5       1대
출도
"""

# 정류장 미리 계산
# 리스트로 제작

import sys
sys.stdin = open('input.txt')

'''
# 1. 모든 노선 체크
def bus_count(bus_stop):
    cnt = 0

    for i in range(N):
        if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
            cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 버스 노선 수

    bus_route = []  # 버스 노선들을 저장해 놓을 리스트

    for i in range(N):
        A, B = map(int, input().split())
        bus_route.append((A, B))

    P = int(input())    # 내가 확인하고 싶은 정류장의 갯수
    ans = []    # 버스 수를 저장해 놓을 리스트

    for i in range(P):
        C = int(input())
        ans.append(bus_count(C))

    print('#{}'.format(tc), end=' ')
    print(' '.join(map(str, ans)))
'''

'''
# 2. 정류장 미리 계산
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 버스 노선 수

    start = [0] * 5001   # 출발 정류장 표시
    end = [0] * 5001    # 도착 정류장 표시
    bus_stop = [0] * 5001   # 계산한 버스 표시

    for i in range(N):
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1

    # 버스 계산 완료
    for i in range(len(bus_stop)-1):
        bus_stop[i+1] = bus_stop[i] + start[i+1] - end[i]

    P = int(input())
    print('#{}'.format(tc), end=' ')
    for i in range(P):
        C = int(input())    # 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()
'''

'''
# 3. 정류장 미리 계산
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 버스 노선 수

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B+1):
            bus_stop[j] += 1    # 지나가는 곳 누적

    P = int(input())
    print('#{}'.format(tc), end=' ')
    for i in range(P):
        C = int(input())  # 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()
'''