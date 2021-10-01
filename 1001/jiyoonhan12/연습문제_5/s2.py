"""
연습문제 5. 부분 집합의 합 구현

5-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기
"""

# 시간 너무 오래걸리는데?! 이거아닌거같음...

def powerset(n, k):  # n: 원소의 개수, k: 현재 depth
    global subset, check
    if k == n:
        temp_sum = 0
        temp = []
        for j in range(n):
            if check[j] == 1:
                temp_sum += nums[j]
                temp.append(nums[j])
        if temp_sum == 0:
            subset.append(temp)
    else:
        for i in range(n):
            check[i] = 1
            powerset(n, k+1)
            check[i] = 0

cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]  # 원소의 포함여부 저장 -> 0 혹은 1
subset = []

powerset(N, 0)
print(subset)

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