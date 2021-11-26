import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(start):
    visited = [0]*(max_val+22)
    visited[start] = 1

    q = deque([start])

    while q:
        pos = q.popleft()
        if pos == M:
            return visited[pos]-1

        for next_pos in [pos+1, pos-1, pos*2, pos-10]:
            if 0 < next_pos < max_val+22 and not visited[next_pos]:
                q.append(next_pos)
                visited[next_pos] = visited[pos]+1

for T in range(int(input())):
    N, M = map(int, input().split())
    max_val = max(N, M)
    print('#{} {}'.format((T+1), bfs(N)))

#1 3
#2 4
#3 8