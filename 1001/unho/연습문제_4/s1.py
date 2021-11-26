"""
연습문제 4. 순열

4-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

nums = [1, 2, 3]

for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            for k in range(len(nums)):
                if k != i and k != j:
                    print(nums[i], nums[j], nums[k])


"""
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

###################################################
# 재귀
print('\n--- recursion ---\n')

def perm(idx):
    if idx == len(nums):
        print(*arr)
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = 1
            arr[idx] = nums[i]
            perm(idx+1)
            visited[i] = 0

arr = [0] * len(nums)
visited = [0] * len(nums)
perm(0)


###################################################
# 재귀 2
print('\n--- recursion 2 ---\n')

def perm_2(n, k, m):
    global cnt
    if m == 0:
        print(*arr)
        return
    
    for i in range(k):
        if not visited[i]:
            visited[i] = 1
            arr[n] = nums[i]
            perm_2(n+1, k, m-1)
            visited[i] = 0


nums = [1, 2, 3, 4, 5]
arr = [0]*3
visited = [0] * len(nums)

perm_2(0, len(nums), 3)