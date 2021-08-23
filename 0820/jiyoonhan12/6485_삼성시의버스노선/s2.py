import sys
sys.stdin = open('input.txt')

# 1. 모든 노선 체크
def bus_count(bus_stop):
    cnt = 0

    for i in range(N):
        if route[i][0] <= bus_stop <= route[i][1]: # 정류장이 시작점과 끝점 사이에 있는지
            cnt += 1

    return cnt

T = int(input())

for t in range(1, T+1):
    N = int(input())

    route = []

    for i in range(N):
        A, B = map(int, input().split())
        route.append((A, B))

    # 내가 확인하고 싶은 정류장의 개수
    P = int(input())
    ans = [] # 버스 수를 저장해 놓을 리스트

    for i in range(P):
        C = int(input())
        ans.append(bus_count(C))

    print('#{}'.format(t), end=' ')
    print(' '.join(map(str, ans)))