import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
# print(N, M)
new_list = [[0]*M for i in range(N)]
# print(new_list)
cnt = 0
for i in range(N):
    for j in range(M):
        new_list[i][j] += cnt
        cnt += 1
print(new_list)
