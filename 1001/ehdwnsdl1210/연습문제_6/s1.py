"""
연습문제 6. Baby-gin
6-1) 반복문

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

def check_babygin(numbers):
    i = 0
    inp = 0
    tri = 0
    run = 0



# arr = [6, 6, 7, 7, 6, 7] # 1
arr = [1, 2, 4, 7, 8, 3]   # 0
print(check_babygin(arr))