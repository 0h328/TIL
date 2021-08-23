import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N = int(input())
    bns = list(map(int, input().split()))
    result = 0

    if 2 <= N <= 10000:
        for i in range(N):
            max_sell = 0
            for j in range(i+1, N):
                if bns[j] - bns[i] <= 10000 and max_sell < bns[j] - bns[i]:
                    max_sell = bns[j] - bns[i]
            result += max_sell
        result = str(result)

        print("#{} {}".format(num+1, result))