import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    cnt = 0
    pair = 0

    for i in range(N):
        while True:
            if cnt == M or A[i] <= B[cnt]:
                pair += cnt
                break
            else:
                cnt += 1

    print(pair)