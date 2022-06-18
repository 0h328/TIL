import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for i in range(2, N):
        ans = max(ans, abs(arr[i]-arr[i-2]))

    print(ans)

# 통나무가 원으로 연결됨 (idx 0이랑 idx n-1이랑 연결)
# idx를 두 칸 차이의 최대로 원을 구성하면 됨.
