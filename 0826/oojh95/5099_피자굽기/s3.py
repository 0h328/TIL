import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    result = []
    for i in range(len(Ci)):
        for j in range(6, -1, -1):
            if 2**j <= Ci[i]:
              result.append(j+1)
              break
    cnt = sorted(result[:N])

    for i in range(N, M):
        if result[i] + cnt[i-N] < max(cnt):


        result[i] += cnt[i-N]
    print(result)
