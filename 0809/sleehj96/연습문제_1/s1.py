import sys
sys.stdin = open('input.txt')

#1. 숫자
num = int(input())
# print(num)
# 예시 출력
# print('#{}'.format(num))

#2. 리스트
print(input().split())
# print(list(map(int, input().split())))

#3. 이차원 리스트
N = int(input()) # 3

print(N)

for _ in range(N):
    # N번 반복을 돌리면 한 줄의 모든 값을 리스트로
    nums = list(map(int, input().split()))
print(nums)

