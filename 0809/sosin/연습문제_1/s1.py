import sys
sys.stdin = open('input.txt')

# 1. 숫자
num = int(input())
print(num)

print('#{}'.format(num))

# 2. 리스트
print(list(map(int, input().split())))

# 3. 이차원배열
N = int(input())
# my_list = []
# for _ in range(N):
#     my_list.append(list(map(int, input().split())))

# 심플입력
my_list = [list(map(int, input().split())) for _ in range(N)]

print(my_list)
