import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

# 풀이1
tmp = []
for i in range(N, 0, -1):
    tmp.insert(arr[i-1], i)   # .insert(idx, 값)

print(tmp)

# 풀이2
# tmp = [0] * N
#
# for i in range(N):
#     cnt = 0
#     for j in range(N):
#         if tmp[j] == 0 and cnt == arr[i]:
#             tmp[j] = i+1
#             break
#         elif tmp[j] == 0:
#             cnt += 1
#
# print(*tmp)

# 7-6-5-4-3-2-1
# 0-0-2-1-1-1-6
# [7]-[6,7]-[6,7,5]-[6,4,7,5]-[6,3,4,7,5]-[6,2,3,4,7,5]-[6,2,3,4,7,5,1]

# 4-3-2-1
# 0-1-1-2
# [4]-[4,3]-[4,2,3]-[4,2,1,3]