"""
연습 문제2. 선택 정렬 (반복 & 재귀)

선택 정렬을 반복과 재귀버전으로 구현하시오.
"""

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

# 반복(for)
def selection_sort_for(my_list):
    for i in range(len(my_list)):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

# selection_sort_for(my_list)
print(my_list)  # [1, 2, 2, 3, 3, 5, 5, 7, 8, 9]


#######################################################################################


# 재귀 - 추가 파라미터 구성 가능
def selection_sort_recursion(pivot, idx, min_idx):
    if idx >= len(my_list):                 # 검색하는 인덱스가 범위 넘어가면
        if pivot >= len(my_list):           # 기준 인덱스가 범위 넘어가면
            return                          # 종료

        my_list[pivot], my_list[min_idx] = my_list[min_idx], my_list[pivot]     # 검색 인덱스만 범위 넘어가면, 기준 인덱스의 값과 가장 작은 값과 스왑
        selection_sort_recursion(pivot+1, pivot+2, pivot+1)                     # 다음 기준을 잡고, 검색
        return
    
    if my_list[min_idx] > my_list[idx]:                 # 지금까지 찾은 가장 작은 값보다 현재 값이 더 작으면
        min_idx = idx                                   # 인덱스 값 갱신
    selection_sort_recursion(pivot, idx+1, min_idx)     # 다음 인덱스 검색
    

selection_sort_recursion(0, 1, 0)
print(my_list)  # [1, 2, 2, 3, 3, 5, 5, 7, 8, 9]