import sys
sys.stdin = open('input.txt')

# 1. 숫자
num = int(input())
# print(num)
# 예시출력
print('#{}'.format(num))


# 2. 리스트
# print(input())
# print(input().split())
# print(list(map(int, input().split())))

# nums = list(map(int, input().split()))
# # for num in nums:
# #     print(num)


# 3. 2차원 리스트

N = int(input())
# 정석
# my_nums = []
#
# for _ in range(N):
#     N번 돌리며 한 줄의 모든 값을 리스트로 만들자
#     nums = list(map(int, input().split()))
#     my_nums.append(nums)
# print(my_nums)

# 단축된 코드
# numbers = [list(map(int, input().split())) for _ in range(N)]
# print(numbers)