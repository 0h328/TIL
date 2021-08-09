import sys
sys.stdin = open('input.txt')

#1. 숫자
num = int(input())
print('#{}'.format(num))

# ctrl + shift + f10 / 우클릭 + run => 출력

#2. 리스트
nums = list(map(int, input().split()))

for num in nums:
    print(num)


#3. 이차원 리스트
N = int(input())

# my_nums = []
# for _ in range(N):
    # N번 반복을 돌리며 한 줄의 모든 요소 값을 리스트로 만들자.
#     nums = list(map(int, input().split()))
#     my_nums.append(nums)
# print(my_nums)

# 조금 더 심플한 버전
numbers = [list(map(int, input().split())) for _ in range(N)]
print(numbers)