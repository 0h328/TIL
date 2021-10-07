import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()

    cnt = 0
    for i in range(m):
        target = b[i]
        left = 0
        right = n-1
        turn = 0  # 중앙기준 생각 방향 설정필요
        while left <= right:
            mid = (left+right)//2
            if a[mid] == target:
                cnt += 1
                break
            elif a[mid] > target:
                right = mid-1
                if turn == -1:
                    break
                turn = -1
            else:
                left = mid+1
                if turn == 1:
                    break
                turn = 1
    print('#{} {}'.format(tc+1, cnt))