"""
연습문제 5. 순열

5-2) 재귀로 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 재귀 함수를 활용하여 구현하시오.

** 각 자리를 어떻게 확정 시킬 것인가에 초점을 맞춰 구현해보세요.
** swap하는 방식과 방문 처리를 하는 방식으로 모두 구현해보세요.
"""

"""
    n = 0                            |1|2|3|
                            /           |             \
    n = 1           |1|2|3|          |2|1|3|        |3|2|1|
                    /    \           /     \        /     \
    n = 2       |1|2|3| |1|3|2|  |2|1|3| |2|3|1| |3|2|1| |3|1|2|

                          자리가 확정되면 출력(n == k)  
"""


# 1. swap
def perm_swap(n, k):                              # n: 숫자를 결정 할 인덱스/자리(결정한 개수) / k: 순열의 길이
    if n == k:                                    # 접근하려는 인덱스가 배열(순열의 길이)의 크기와 같다?
        print(*nums)                              # 모든 자리 확정 만들어지면 출력
    else:
        for i in range(n, k):                     # i -> 자기 자신 부터 ~ 맨 마지막(k-1)까지 순서대로 교환
            nums[n], nums[i] = nums[i], nums[n]   # 현재 숫자 유지부터, 오른쪽 끝까지 교환 (처음에는 자기 자신과 교환)
            perm_swap(n+1, k)                     # 다음번 자리 결정하러 이동(n개 결정)
            nums[n], nums[i] = nums[i], nums[n]   # 교환전으로 다시 복구 (반복 과정 안에서 return 하고 돌아온 이후의 작업을 잘 살펴볼 것)

nums = [1, 2, 3]
perm_swap(0, 3)

print('---------------------------------------')


# 2. visited
def perm_visited(k):
    if n == k:
        print(*sel)
        return
    else:
        for i in range(n):
            if visited[i]: continue    # 이미 체크한 자리는 넘어가고
            visited[i] = 1             # 자리 체크
            sel[k] = nums[i]           # 그때의 값을 sel의 k번째에 할당
            perm_visited(k+1)          # 다음 자리 확인
            visited[i] = 0             # 원상 복구


nums = [1, 2, 3]
n = len(nums)
visited = [0] * n                      # 체크 했는지 여부 확인
sel = [0] * n                          # 실제 값 할당
perm_visited(0)