"""
연습문제 5. 부분 집합의 합 구현

5-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기

** 비트 연산
- 원소 수에 해당하는 N개의 비트열을 활용
- n번째 비트값이 1이면 n번째 원소가 '포함'되었음을 의미

0   0 0 0 0   {A, B, C, D}
1   0 0 0 1   {A}
2   0 0 1 0   {B}
3   0 0 1 1   {B, A}
...........
14  1 1 1 0   {D, C, B}
15  1 1 1 1   {D, C, B, A}
"""


# 1. 재귀 활용
def print_set(n):
    global cnt_subset
    sum_of_subset = 0
    for i in range(n):
        if check[i] == 1:                            # 포함된 요소는
            sum_of_subset += nums[i]                 # 실제 위치(nums[i])에서 값을 가져와 합하자

    if sum_of_subset == 0:                           # 합이 0인 경우에
        cnt_subset += 1
        print('{}: '.format(cnt_subset), end='')     # (참고) 생성되는 부분 배열의 개수 출력

        for i in range(n):                           # 각 부분 배열의 원소를 돌며 그 값을 출력하자
            if check[i] == 1:                        # (check[i]가 1이면 포함되었다는 의미 -> 출력!)
                print('{} '.format(nums[i]), end='')
        print()


def powerset(n, k):                     # n: 원소의 개수, k: 현재 depth
    if n == k:
        print_set(n)
    else:
        check[n] = 1                     # n번 요소를 포함시킴
        powerset(n + 1, k)               # 다음 요소 포함 여부 결정
        check[n] = 0                     # n번 요소를 포함시키지 않음
        powerset(n + 1, k)               # 다음 요소 포함 여부 결정


cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]             # 원소의 포함여부 저장 -> 0 혹은 1

powerset(0, N)

print('------------------------------------------------')

# 2-1. 비트 연산 활용
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)

for i in range(1 << N):             # 부분집합의 개수
    my_sum = []
    for j in range(N):              # n개의 원소와 비교를 할 것 (원소의 수만큼 비트 비교)
        if i & (1 << j):            # i의 j 번째 비트가 1인 경우(&) j 번째 원소 출력 -> i의 j번 비트 검사
            my_sum.append(nums[j])  # 1인 경우는 그 자리에 해당하는 nums의 값을 리스트에 담자
    if sum(my_sum) == 0:            # 합이 0인 경우 출력
        print(*my_sum)

print('------------------------------------')

# 2-2. 비트 연산 활용
nums2 = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums2)

for i in range(1 << N):             # 부분집합의 개수
    my_sum = 0
    for j in range(N):              # n개의 원소와 비교를 할 것 (원소의 수만큼 비트 비교)
        if i & (1 << j):            # i의 j 번째 비트가 1인 경우(&) j 번째 원소 출력 -> i의 j번 비트 검사
            my_sum += nums2[j]      # 1인 경우는 그 자리에 해당하는 nums의 값을 리스트에 담자
    if my_sum == 0:                 # 합이 0인 경우 출력
        for j in range(10):
            if i & (1 << j):
                print(nums[j], end=' ')
        print()