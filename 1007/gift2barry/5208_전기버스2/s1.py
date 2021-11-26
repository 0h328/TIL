import sys
sys.stdin = open('input.txt')

'''
디버깅시간 
구현시간 49분
thought process: 15분
인덱스위치는 피벗 활용하여 이동하며,
총 인덱스 길이에서, 피벗에 위치한 원소 길이를 빼주면서
충전 경우의 수들을 탐색.
최소 충전횟수를 갱신해 나가면서,
가지치기로 최소 충전횟수를 넘기면, 더이상 보지 않기로 하자.

용량은 중첩되지 않고, 교체된다
'''


def dfs(idx, move, cnt):    # 현재 위치 인덱스, 이동가능거리, 현재 충전횟수
    global ans

    if move >= N - idx:     # 앞으로 이동 가능 길이만큼 이동하여 도착하면 끝
        ans = cnt           # 정답 갱신

    else:
        # for i in range(idx+1, idx + move + 1):   # 1. 현재위치로부터 이동 가능한 거리의 모든 정류장 방문
        for i in range(idx + move, idx, -1):       # 2. 최대한 멀리 부터 확인하며 검사하면 왠지 빨리 찾을 수 있을듯 한데.. 끊는 타이밍을 어떻게..
            if cnt+1 < ans:               # 현재 최소 주유량보다 많이 주유하려는 순간 탐색 stop (가지치기)
                dfs(i, arr[i], cnt+1)
    return


for tc in range(1, int(input())+1):
    arr = tuple(map(int, input().split()))
    N = arr[0]          # 이동해야하는 총 길이
    ans = 10000000000   # 최소 충전횟수 저장 변수
    dfs(1, arr[1], 0)   # 출발지점 인덱스, 이동 가능 횟수, 충전 횟수 카운터
    print('#{} {}'.format(tc, ans))