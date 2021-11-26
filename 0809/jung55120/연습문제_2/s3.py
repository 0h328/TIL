import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
new_list = [[0] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        new_list[i][j] = cnt
        cnt += 1
print(new_list)