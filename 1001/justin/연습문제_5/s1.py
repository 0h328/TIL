"""
연습문제 5. 부분 집합 구현

5-1) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2} 의 모든 부분 집합 구하기
"""

def print_set(n):
    global cnt_subset
    cnt_subset += 1
    print('{}: '.format(cnt_subset), end='')  # 생성되는 부분 집합 개수

    for i in range(n):                        # 각 부분 배열의 원소를 순회하며
        if check[i] == 1:                     # check[i]가 1이면 포함 되어있음을 의미하니
            print(nums[i], end=' ')           # 출력
    print()

def powerset(n, k):            # n: 현재 depth, k: 원소의 개수
    if n == k:
        print_set(n)
    else:
        check[n] = 1           # n번 요소를 포함시킴
        powerset(n+1, k)       # 다음 요소 포함 여부 결정하기 위한 호출
        check[n] = 0           # n번 요소를 포함시키지 않음
        powerset(n+1, k)       # 다음 요소 포함 여부 결정하기 위한 호출


cnt_subset = 0                                     # 생성되는 부분집합의 수 확인
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]                      # 원소의 포함(0 혹은 1) -> check의 인덱스 -> nums의 인덱스에 해당하는 값의 포함 여부
powerset(0, N)