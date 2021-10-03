"""
연습문제 6. Baby-gin
6-2) 재귀

베이비진이면 1
베이비진이 아니면 0
"""

"""
baby gin
arr = [6, 6, 7, 7, 6, 7]
arr = [0, 5, 4, 0, 6, 0]

baby gin x
arr = [1, 2, 4, 7, 8, 3]
arr = [1, 0, 1, 1, 2, 3]
"""

def baby_gin(n, k):
    global ans
    if k == n:
        front = arr[:3]
        back = arr[3:]
        if front[0] == front[1] == front[2] and back[0] + 2 == back[1] + 1 == back[2]:
            ans =  1
        if front[0] + 2 == front[1] + 1 == front[2] and back[0] + 2 == back[1] + 1 == back[2]:
            ans = 1
        if front[0] == front[1] == front[2] and back[0] == back[1] == back[2]:
            ans = 1
        if front[0] + 2 == front[1] + 1 == front[2] and back[0] == back[1] == back[2]:
            ans = 1
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            baby_gin(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]


arr = [1, 0, 1, 1, 2, 3]
ans = 0
baby_gin(6, 0)
print(ans)