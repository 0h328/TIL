"""
연습문제 4. 순열

4-2) 재귀로 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 재귀 함수를 활용하여 구현하시오.

** 각 자리를 어떻게 확정 시킬 것인가에 초점을 맞춰 구현해보세요.
** swap하는 방식과 방문 처리를 하는 방식으로 모두 구현해보세요.
"""

#0. 순열이 생성되는 과정 그려보기
# 순열이 생성되는 과정을 반드시 먼저 손으로 그려보고 코드 작성

#1. swap
def perm_swap(n, k):
    if k == n:
        print(*nums)
    else:
        for i in range(k, n):
            nums[i], nums[k] = nums[k], nums[i]
            perm_swap(n, k+1)
            nums[i], nums[k] = nums[k], nums[i]

nums = [1, 2, 3]
perm_swap(3, 0)

#2. visited
def perm_visited(n, d, per):
    if d == n:
        print(*per)
    else:
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                perm_visited(n, d+1, per+ [nums[i]])
                used[i] = False

# nums = [1, 2, 3]
used = [False for _ in range(len(nums))]

# print(perm_visited(3, 0, []))

"""
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
3 1 2
"""