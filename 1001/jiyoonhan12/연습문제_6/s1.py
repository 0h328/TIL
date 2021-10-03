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
    front =  [-1, -1, -1]
    back = [-1, -1, -1]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                for k in range(len(numbers)):
                    if k != i and k != j:
                        for l in range(len(numbers)):
                            if l != i and l != j and l != k:
                                for m in range(len(numbers)):
                                    if m != i and m != j and m != k and m != l:
                                        for n in range(len(numbers)):
                                            if n != i and m != j and m != k and m != l and n != m:
                                                front[0] = numbers[i]
                                                front[1] = numbers[j]
                                                front[2] = numbers[k]
                                                back[0] = numbers[l]
                                                back[1] = numbers[m]
                                                back[2] = numbers[n]
                                                front.sort()
                                                back.sort()
                                                if front[0] + 2 == front[1] + 1 == front[2] and back[0] == back[1] == \
                                                        back[2]:
                                                    return 1
                                                if front[0] + 2 == front[1] + 1 == front[2] and back[0] + 2 == back[
                                                    1] + 1 == back[2]:
                                                    return 1
                                                if front[0] == front[1] == front[2] and back[0] + 2 == back[1] + 1 == \
                                                        back[2]:
                                                    return 1
                                                if front[0] == front[1] == front[2] and back[0] == back[1] == back[2]:
                                                    return 1
    else:
        return 0


# arr = [6, 6, 7, 7, 6, 7] # 1
arr = [1, 2, 4, 7, 8, 3]   # 0
print(check_babygin(arr))