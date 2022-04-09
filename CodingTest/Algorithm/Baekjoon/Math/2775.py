import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    ans = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            ans[j] += ans[j-1]

    print(ans[-1])