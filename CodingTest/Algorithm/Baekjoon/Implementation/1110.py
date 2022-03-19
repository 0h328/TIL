import sys
sys.stdin = open('input.txt')

arr = [list(input()) for _ in range(8)]

cnt = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 or i % 2 and j % 2:
            if arr[i][j] == 'F':
                cnt += 1

print(cnt)