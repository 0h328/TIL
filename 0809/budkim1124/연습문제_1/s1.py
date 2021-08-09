# txt 파일을 읽어온다.
import sys
sys.stdin = open('input.txt')

num = int(input())
# print(num)
# 예시 출력
print('#{}'.format(num))

#2. 리스트
# print(input())
print(list(map(int, input().split())))

#3. 이차원 리스트
N = int(input())

my_nums = []
for _ in range(N):
    # N번 반복을 돌리며 한 줄의 모든 값을 리스트로 만들자
    nums = list(map(int, input().split()))
    my_nums.append(nums)

print(my_nums)


# 조금 더 심플한 버전
# numbers = [list(map(int, input().split())) for _ in range(N)]
# print(numbers)
#





