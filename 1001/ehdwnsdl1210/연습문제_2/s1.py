"""
연습 문제2. 선택 정렬 (반복 & 재귀)

선택 정렬을 반복과 재귀버전으로 구현하시오.
"""

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

# # 반복(for)
# def selection_sort_for(my_list):
#     n = len(my_list)
#
#     for i in range(0, n-1):
#         min_value = i
#         for j in range(i + 1, n):
#             if my_list[min_value] > my_list[j]:
#                 min_value = j
#             my_list[min_value], my_list[i] = my_list[i], my_list[min_value]
#
#
# selection_sort_for(my_list)
# print(my_list)  # [1, 2, 2, 3, 3, 5, 5, 7, 8, 9]


#######################################################################################


# 재귀 - 추가 파라미터 구성 가능
def selection_sort_recursion(my_list):
    if:

    else:



selection_sort_for(my_list)
print(my_list)  # [1, 2, 2, 3, 3, 5, 5, 7, 8, 9]