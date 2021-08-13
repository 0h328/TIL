def binary_recursion(start, end, goal):
    # start -> 시작 / end -> 목표 지점 / goal -> 찾고자 하는 페이지
    mid = (start + end) // 2
    if mid == goal:  # Base Case
        return 1

    elif mid > goal:  # 만약 중간값이 목표보다 위에 있으면 끝을 중간으로 이동시켜 다시 탐색
        return binary_recursion(start, mid, goal) + 1  # 함수를 다시 호출하는 것은 책을 다시 한번 폈다고 생가해보자(+1)
    else:  # 만약 중간값이 목표보다 아래에 있으며 있으면 시작을 중간으로 이동시켜 다시 탐색
        return binary_recursion(mid, end, goal) + 1


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    count_a = binary_recursion(1, P, A)
    count_b = binary_recursion(1, P, B)

    ans = 0

    if count_a < count_b:
        ans = 'A'
    elif count_a > count_b:
        ans = 'B'
    print('#{} {}'.format(tc, ans))