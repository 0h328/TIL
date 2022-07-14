import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

straw = [int(sys.stdin.readline()) for _ in range(N)]
straw.sort(reverse=True)

ans = 0
for i in range(N-2):
    if straw[i] < straw[i+1] + straw[i+2]:
        ans = straw[i] + straw[i+1] + straw[i+2]
        break
    else:
        ans = -1

print(ans)