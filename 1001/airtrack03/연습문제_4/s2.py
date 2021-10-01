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
    if n == k:
        print(*nums)
        return
    for j in range(k, n):
        nums[k], nums[j] = nums[j], nums[k]
        perm_swap(n, k+1)
        nums[k], nums[j] = nums[j], nums[k]

nums = [1, 2, 3]
perm_swap(3, 0)

print('#####')
#2. visited
visited = [0] * 3
p = [0] * 3
def perm_visited(n, k):
    if k == n:
        print(*p)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            p[k] = nums[i]
            perm_visited(n, k+1)
            visited[i] = 0


nums = [1, 2, 3]
perm_visited(3, 0)

"""
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
3 1 2
"""