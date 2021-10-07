"""
연습문제 5. 순열

5-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

nums = [1, 2, 3]

for i in range(3):
    for j in range(3):
        if i != j:
            for k in range(3):
                if i != k and j != k:
                    print(i+1, j+1, k+1)

"""
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""



"""
연습문제 5. 순열

5-2) 재귀로 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 재귀 함수를 활용하여 구현하시오.

** 각 자리를 어떻게 확정 시킬 것인가에 초점을 맞춰 구현해보세요.
** swap하는 방식과 방문 처리를 하는 방식으로 모두 구현해보세요.
"""
#0. 순열이 생성되는 과정 그려보기
# 순열이 생성되는 과정을 반드시 먼저 손으로 그려보고 코드 작성

print('----- recursion (swap) -----')
#1. swap
def perm_swap(n, k):
    if n >= k:
        for i in range(3):
            print(nums[i], end=' ')
        print()
        return

    for i in range(n, 3):
        nums[i], nums[n] = nums[n], nums[i]
        perm_swap(n+1, k)
        nums[i], nums[n] = nums[n], nums[i]

nums = [1, 2, 3]
perm_swap(0, 3)


print('----- recursion (visited) -----')
#2. visited
def perm_visited(idx):
    if idx >= N:
        for i in range(N):
            print(answer[i], end=' ')
        print()
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            answer[idx] = nums[i]
            perm_visited(idx+1)
            visited[i] = 0

nums = [1, 2, 3]
visited = [0] * 3
answer = [0] * 3
N = len(nums)
perm_visited(0)

"""
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
3 1 2
"""



"""
연습문제 5. 순열

5-3) 5개의 숫자 중 3자리의 순열 생성하기
[1, 2, 3, 4, 5]에서 3자리의 순열을 재귀 함수를 활용하여 구현하시오.
"""

print('----- recursion (5P3) -----')
def perm(n, k, m): 		# n: 숫자를 결정 할 자리 인덱스, k: 순열의 길이, m: 주어진 숫자의 개수
    if m <= 0:
        for i in range(3):
            print(answer[i], end=' ')
        print()
        return
    
    for i in range(k):
        if not visited[i]:
            visited[i] = 1
            answer[n] = nums[i]
            perm(n+1, k, m-1)
            visited[i] = 0


nums = [1, 2, 3, 4, 5]
visited = [0] * len(nums)
answer = [0] * 3
perm(0, len(nums), 3)

"""
1 2 3 
1 2 4 
1 2 5 
1 3 2 
1 3 4 
1 3 5 
1 4 3 
1 4 2 
1 4 5 
1 5 3 
1 5 4 
1 5 2 
2 1 3 
2 1 4 
2 1 5 
2 3 1 
2 3 4 
... 생략
"""