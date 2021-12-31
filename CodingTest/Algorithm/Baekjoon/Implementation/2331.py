import sys
sys.stdin = open('input.txt')

# 풀이1
# A, P = input().split()
# p = int(P)
#
# tmp = [int(A)]
#
# while tmp.count(tmp[-1]) < 2: # list의 마지막 원소가 2개가 되면 반복되므로 종료
#     cnt = 0                   # 각 자리의 숫자를 p번 곱해서 더하기 위한 변수
#     K = tmp[-1]               # list의 마지막 원소를 K로 지정하고
#     k = str(K)                # K를 str화
#     for i in range(len(k)):   # k의 길이만큼 반복문 돌고
#         cnt += int(k[i])**p   # cnt에 K를 int화해서 P번 곱하고
#     tmp.append(cnt)           # tmp에 추가
#
# res = tmp[0:tmp.index(tmp[-1])]   # 0부터 tmp의 마지막 원소까지 slice해서
# print(len(res))   # 길이 출력

# 풀이2
A, P = map(int, input().split())

nums = [A]                      # A를 먼저 list에 넣고
while True:
    tmp = 0                     # 곱한 수들의 합을 구하기 위한 변수
    for s in str(nums[-1]):     # list 마지막 idx에 있는 수를 str화하고 반복
        tmp += int(s) ** P      # 각 자리의 숫자를 p번 곱하여 tmp에 더하기
    if tmp in nums:             # tmp가 이미 nums에 있으면 반복되는 수
        break                   # 종료

    nums.append(tmp)            # nums에 tmp를 추가
print(nums.index(tmp))          # index 특성상 배열에 첫번째 tmp의 idx를 출력