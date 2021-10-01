"""
연습문제 5. 부분 집합의 합 구현

5-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기
"""

def powerset(n):  # n: 원소의 개수, k: 현재 depth
    global cnt_subset
    for i in range(1 << n):
        total = 0
        for j in range(n):
            if i & (1 << j):
                total += nums[j]
                check[j] = 1
        if not total:
            cnt_subset += 1
            print(cnt_subset, end=': ')
            for k in range(n):
                if check[k]:
                    print(nums[k], end=' ')
                    check[k] = 0
            print()


cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]  # 원소의 포함여부 저장 -> 0 혹은 1
powerset(N)

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