import sys
sys.stdin = open('input.txt')

N = int(input())

number = [list(map(int, input().split())) for _ in range(N)]

# 1. 행우선
for i in range(len(number)):
    for j in range(len(number[i])):
        print(number[i][j], end = ' ')


# 2. 열우선 (먼저 고정하는 것은 바깥 for문)
for i in range(len(number[0])):
    for j in range(len(number)):
        print(number[j][i], end = ' ')


# 3. 지그재그 (i가 짝수일 때 / i가 홀수일 때)
for i in range(len(number)):
    if i % 2:
        for j in range(len(number[0])-1, -1, -1):
            print(number[i][j], end= ' ')
    else:
        for j in range(len(number[0])):
            print(number[i][j], end= ' ')


# 4. 전치행렬
for i in range(len(number)):
    for j in range(len(number)):
        if i < j:
            number[i][j], number[j][i] = number[j][i], number[i][j]
print(number)


# 대각 숫자 삽입
# n = 10
# arr = [[0] * n for _ in range(n)]
# for i in range(n):      # 우하 대각
#     arr[i][i] = 1
#
# for i in range(n):      # 좌하 대각
#     arr[i][n-i-1] = 2   # (!)
#
# for lst in arr:     # 출력(!)
#     print(*lst)     # 언패킹(!)


# 선택 정렬 (1개씩 해보고 나중에 for로 전체를 감싸면?!)
# for 바깥 : N-1번 반복
# for 안 : 찾고 옮기기
# 인덱스가 1씩 증가
# 최소값의 인덱스를 찾아라!
arr = [6, 5 ,3 ,8 ,1 ,7 ,4]
M = len(arr)

for i in range(M-1):
    min_idx = i
    for j in range(i + 1, M):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)

# min_idx = 0
# for i in range(1, M):
#     if arr[min_idx] > arr[i]:
#         min_idx = i
# arr[0], arr[min_idx] = arr[min_idx], arr[0]
# print(arr)
#
# min_idx = 1
# for i in range(2, M):
#     if arr[min_idx] > arr[i]:
#         min_idx = i
# arr[1], arr[min_idx] = arr[min_idx], arr[1]
# print(arr)
#
# min_idx = 2
# for i in range(3, M):
#     if arr[min_idx] > arr[i]:
#         min_idx = i
# arr[2], arr[min_idx] = arr[min_idx], arr[2]
# print(arr)