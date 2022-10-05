import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

ans = N
for i in range(N):
    arr[i] -= B
    if arr[i] > 0:
        if arr[i] % C > 0:
            ans += arr[i]//C + 1
        else:
            ans += arr[i]//C

print(ans)