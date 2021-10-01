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
rr = [1, 0, 1, 1, 2, 3]
"""

cnt = [0] * 10
def check_babygin(numbers):
    for num in numbers:
        cnt[num] += 1

    for i in range(10):
        if cnt[i] > 2:
            cnt[i] -= 3 * (cnt[i] // 3)

    for i in range(8):
        if cnt[i]:
            if cnt[i+1] and cnt[i+2]:
                sub_val = min(cnt[i], cnt[i+1], cnt[i+2])
                for j in range(3):
                    cnt[i+j] -= sub_val

    if sum(cnt):
        return 0
    return 1

arr = [6, 6, 7, 7, 6, 7] # 1
# arr = [1, 2, 4, 7, 8, 3]   # 0
print(check_babygin(arr))