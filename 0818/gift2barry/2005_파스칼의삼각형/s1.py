import sys
sys.stdin = open('input.txt')

def pascal(n):
    memo[n] = [1, sum(memo[n-1]), 1]     # (인덱스값 - 1) = 가운데 숫자 개수
    print(memo[n])


for i in range(1, 3):
    n = i
    memo = [0] * (i + 1)
    memo[0] = [1]
    memo[1] = [1, 1]
    print(1)
    if i == 0 or i == 1:
        if memo[n] == 1:    #첫번째 값이면
            print(memo[n])
        elif memo[n] == [1, 1]:
            print(memo[n])
    else:
        pascal(i)


# # memorization 이용한 풀이 패작 2
# def unpack(nums):
#     for i in nums:
#         print(i, end='')

# def pascal(n):
#     if n == 1:              # n 이 1이면 항상 1
#         row = [1]
#         print(row[0])          # 고로 1 프린트
#     else:
#         previous_row = pascal(n - 1)    # 이전 pascal 함수 리턴값을 변수에 할당
#         pairs = zip(previous_row[:-1], previous_row[1:])    # 노트 사진 참조
#         row = [1] + list(map(sum, pairs)) + [1]     # 양옆은 항상 1 이므로 더해준다.
#         unpack(row)
#     return row

# 패작 1
# def pascal(n):
#     if n == 0:
#         print(1)
#     elif n == 1:
#         mid_num = 2
#         print(1, 1)
#     else:
#         for i in range(n-1):

# for tc in range(1, int(input())+1):
#     pascal(tc)