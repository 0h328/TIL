import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    candy = list(map(int, input().split()))
    d = [0] * N     # 넘겨줄 사탕 기록
    rotate_cnt = 0
    while True:
        for i in range(N):
            if candy[i] % 2:        # 사탕 개수가 홀수면
                candy[i] += 1       # 한개 추가
            d[i] = candy[i] // 2    # 절반을 옆에줌.
        print(d)
        if len(set(candy)) == 1:    # 모든 사탕의 개수가 동일하다면 set[7, 7, 7] = {7}
            print(rotate_cnt)       # 순환 횟수 출력
            break

        for i in range(1, N):                   # 두번째 아이부터
            candy[i] = candy[i] // 2 + d[i-1]   # 첫번째 아이의 사탕 + 세번째 아이한테 줄 사탕 제외 하고 덧셈
        candy[0] = candy[0] // 2 + d[-1]        # 첫번째 아이는 두번째 아이한테 줄 사탕 + 마지막째 아이한테 받을 사탕
        rotate_cnt += 1                         # 순환 횟수 +1