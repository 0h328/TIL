import sys
sys.stdin = open('input.txt')

N = int(input())
arr = sorted(tuple(map(int, input().split())), key=lambda x: x) # 인출시간 적은 순서로 정렬(오름차순)

ans = 0
for i in range(N):
    ans += sum(arr[:i+1])

print(ans)