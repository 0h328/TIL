def binary_search(A_list: list, B_list: list):
    # B_list의 요소가 A_list에 몇 개 있는지 보는게 포인트
    global ans
    for num in B_list:                              # B_list에서 하나씩 값을 꺼내 A_list에 있는지 확인
        left_idx = 0                                # left  -> 시작(0)
        right_idx = N-1                             # right -> 끝(N-1)
        direction = -1                              # 방향 -> 왼쪽: 0, 오른쪽: 1 / 첫 방향은 알 수 없기 때문에 -1로 설정

        while left_idx <= right_idx:                # 왼쪽이 오른쪽을 넘어서기 직전까지
            mid_idx = (left_idx + right_idx) // 2   # middle idx 잡고
            if num == A_list[mid_idx]:              # B_list의 요소가 A_list에 있다면
                ans += 1                            # ans 증가
                break                               # 반복 종료 후 B_list의 다음 숫자가 포함되어 있는지 확인
            elif num > A_list[mid_idx]:             # B_list의 요소가 더 큰 경우
                left_idx = mid_idx + 1              # mid의 범위를 왼쪽으로 설정
                if direction == 0:                  # 이전에도 왼쪽이었다면
                    break                           # 중단
                direction = 0                       # 왼쪽 방향으로 설정
            elif num < A_list[mid_idx]:             # B_list의 요소가 작은 경우
                right_idx = mid_idx - 1             # mid의 범위를 오른쪽으로 설정
                if direction == 1:                  # 이전에도 오른쪽이면 
                    break                           # 중단
                direction = 1                       # 오른쪽 방향으로 설정

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())            # N: A에 속한 정수의 개수, M: B에 속한 정수의 개수
    A = sorted(list(map(int,input().split())))  # N개와 M개의 백만 이하의 양의 정수 -> A는 정렬
    B = list(map(int, input().split()))
    ans = 0                                     # 조건에 맞는 정수의 개수
    binary_search(A, B)
    print('#{} {}'.format(tc, ans))