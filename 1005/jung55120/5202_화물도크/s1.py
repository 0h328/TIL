import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    truck = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            if truck[i][1] > truck[j][1]:
                truck[i], truck[j] = truck[j], truck[i]
    print(truck)