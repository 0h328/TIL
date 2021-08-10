import sys
sys.stdin = open('input.txt')
# sys.stdin.readline()

# 1. 숫자
num = int(input())

# print(num)
# 예시 출력
# print('#{}'.format(num))

# 2. 리스트
# print(input())
# print(input().split())
# print(list(map(int, input().split())))

# 3. 2차원 리스트
N = int(input())

# my_nums = []
# for _ in range(N):
#     # N번 반복을 돌리며 한줄의 모든 값을 리스트로 만들자
#     nums = list(map(int, input().split()))
#     # print(nums)
#     my_nums.append(nums)
# print(my_nums)

# 조금 더 심플한 버젼
numbers = [list(map(int, input().split())) for _ in range(N)]
print(numbers)