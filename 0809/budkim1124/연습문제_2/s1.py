# txt 파일을 읽어온다.
import sys
sys.stdin = open('input.txt')

# 행 / 열의 길이 받기
N, M = map(int, input().split())
print(N, M)


arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

#1. 행 우선 선회
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()

print('\n', '2. 열 우선 선회', sep='')
#2. 열 우선 선회
for i in range(M):
    for j in range(N):
        print(arr[j][i], end=' ')
    print()