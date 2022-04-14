import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())
    ans = 0
    for i in range(1, n):
        if i**2 <= n:
            ans += 1
        if i**2 > n:
            break

    print(ans)