# txt 파일을 읽어온다.
import sys
sys.stdin = open('input.txt')

# 행 / 열의 길이 받기
N, M = map(int, input().split())
print(N, M)


arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

#1. 행 우선 순회
arr_row = [list(map(int, input().split())) for _ in range(N)]
print(arr_row)

#2. 열 우선 순회