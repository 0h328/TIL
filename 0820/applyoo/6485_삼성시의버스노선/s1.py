import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    station = [int(input()) for _ in range(P)]
    result = [0] * P # 결과를 저장할 리스트

    for i, j in bus: # 시작 노선, 끝 노선 반복
        for idx in range(P):
            if i <= station[idx] <= j: # 해당 station 번호가 i~j일 경우
                result[idx] += 1 # +1

    print('#{}'.format(test+1), end=' ')
    print(*result)
