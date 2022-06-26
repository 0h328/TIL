import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
pos = list(input())
ans = 0
for idx in range(N):
    if pos[idx] == 'P':
        for i in range(max(idx-K, 0), min(idx+K+1, N)):
            if pos[i] == 'H':
                pos[i] = 0
                ans += 1
                break
print(ans)