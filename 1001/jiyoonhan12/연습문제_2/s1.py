"""
연습 문제2. 선택 정렬 (반복 & 재귀)

선택 정렬을 반복과 재귀버전으로 구현하시오.
"""

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

# 반복(for)
def selection_sort_for(my_list):
    n = len(my_list)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

# selection_sort_for(my_list)
print(my_list)  # [1, 2, 2, 3, 3, 5, 5, 7, 8, 9]


#######################################################################################


# 재귀 - 추가 파라미터 구성 가능
def selection_sort_recursion(my_list):
    if my_list != []:
        min_num = min(my_list)
        my_list.remove(min_num)
        return [min_num] + selection_sort_recursion(my_list)
    else:
        return []


print(selection_sort_recursion(my_list))  # [1, 2, 2, 3, 3, 5, 5, 7, 8, 9]