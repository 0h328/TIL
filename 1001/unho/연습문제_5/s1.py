"""
연습문제 5. 부분 집합 구현

5-1) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2} 의 모든 부분 집합 구하기
"""

def powerset(idx, N):
    if idx == N:
        for i in range(N):
            if visited[i]:
                print(nums[i], end=' ')
        print()
        return

    visited[idx] = 1
    powerset(idx+1, N)
    visited[idx] = 0
    powerset(idx+1, N)
    

nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
visited = [0] * N
powerset(0, N)

"""
-1 3 -9 6 7 -6 1 5 4 -2 
-1 3 -9 6 7 -6 1 5 4 
-1 3 -9 6 7 -6 1 5 -2 
-1 3 -9 6 7 -6 1 5 
-1 3 -9 6 7 -6 1 4 -2 
-1 3 -9 6 7 -6 1 4 
-1 3 -9 6 7 -6 1 -2 
-1 3 -9 6 7 -6 1 
-1 3 -9 6 7 -6 5 4 -2 
-1 3 -9 6 7 -6 5 4 
-1 3 -9 6 7 -6 5 -2 
-1 3 -9 6 7 -6 5 
-1 3 -9 6 7 -6 4 -2 
...
"""

#######################################################################################

"""
연습문제 5. 부분 집합의 합 구현

5-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기
"""

def powerset(n, k):  # n: 원소의 개수, k: 현재 depth
    global cnt_subset

    if n == k:
        li = []
        tmp = 0
        for i in range(k):
            if check[i]:
                tmp += nums[i]
                li.append(nums[i])

        if not tmp:
            cnt_subset += 1
            print(f'{cnt_subset} : ', end='')
            print(*li)

        return

    check[n] = 1
    powerset(n+1, k)
    check[n] = 0
    powerset(n+1, k)

cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]  # 원소의 포함여부 저장 -> 0 혹은 1

powerset(0, N)

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