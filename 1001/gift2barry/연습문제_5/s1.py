"""
연습문제 5. 부분 집합의 합 구현

5-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기
# """
import pprint
# 원소의 합이 0이 되는 부분집합 중복없이 추출
# 문제없이 출력.

# def powerset(k):
#     if k == N:
#         return
#     else:
#         ans.append(tmp[k])
#         powerset(k+1)
#         if sum(ans) == 0:
#             print(ans)
#         ans.pop()
#         powerset(k+1)
#
# nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# tmp = sorted(nums)
# N = len(nums)
# ans = []
# powerset(0)


# # 모든 부분집합 중 원소의 합이 0 이 되는 순열 추출
# 아직 미해결.. 언제쯤 해결될지 모르겠음
def powerset(n, k):  # n: 원소를 채울 리스트 길이, m: 주어진 원소의 개수, k: 현재 depth (ans에 넣은 원소 개수)
    if n == k:
        return
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                ans[k] = nums[i]
                if sum(ans) == 0:
                    tmp.append(ans)
                powerset(n, k+1)
                check[i] = 0

cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]   # 원소의 포함여부 저장 -> 0 혹은 1
ans = [0] * N                   # 저장될
tmp = []
powerset(N, 0)
pprint.pprint(tmp)

"""
1: -1 3 -9 6 7 -6 
2: -1 3 -9 6 -6 5 4 -2 
3: -1 3 -9 6 1 
4: -1 3 -9 7 -6 1 5 
5: -1 3 -9 7 
6: -1 3 -9 5 4 -2 
7: -1 3 6 -6 -2 
8: -1 3 -6 1 5 -2 
9: -1 3 -6 4 
10: -1 3 -2 
11: -1 -9 6 7 -6 1 4 -2 
12: -1 -9 6 7 -6 5 -2 
13: -1 -9 6 -6 1 5 4 
14: -1 -9 6 1 5 -2 
15: -1 -9 6 4 
16: -1 -9 7 -6 5 4 
...
43: 
"""