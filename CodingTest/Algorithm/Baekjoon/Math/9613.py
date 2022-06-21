import sys, math
sys.stdin = open('input.txt')
t = int(input())

for _ in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            ans += math.gcd(arr[i], arr[j])

    print(ans)
