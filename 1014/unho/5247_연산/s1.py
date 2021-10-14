import sys
from collections import deque
sys.stdin = open('input.txt')


# def bfs(num):
#     q = deque([num])
#     visited[num] = 1

#     while q and not visited[M]:
#         node = q.popleft()
#         for e in [node+1, node-1, node*2, node-10]:
#             if e > 0 and e < 1000001 and not visited[e]:
#                 visited[e] = visited[node] + 1
#                 q.append(e)


T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())

#     visited = [0] * 1000001

#     bfs(N)
    
#     print('#{} {}'.format(tc, visited[M]-1))

dp = [1e10] * 1000011
dp[0] = 0
dp[1] = 1
dp[2] = 2

for idx in range(3, 1000001):
    if not idx%2:
        dp[idx] = min(dp[idx-1]+1, dp[idx+1]+1, dp[idx//2]+1, dp[idx+10]+1)
    else:
        dp[idx] = min(dp[idx-1]+1, dp[idx+1]+1, dp[idx+10]+1)


for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(dp[:M+10])
    print(dp[M])