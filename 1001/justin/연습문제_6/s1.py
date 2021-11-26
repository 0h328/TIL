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

def check_babygin(numbers):
    counter = [0 for _ in range(10)]
    is_babygin = 0

    for number in numbers:
        counter[number] += 1

    idx = 0
    while idx < len(counter):
        # print(idx)
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            continue

        if idx < len(counter) - 2:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                is_babygin += 1
                continue

        if is_babygin == 2:
            return 1
        idx += 1
    return 0

# arr = [6, 6, 7, 7, 6, 7] # 1
arr = [1, 2, 4, 7, 8, 3]   # 0
print(check_babygin(arr))