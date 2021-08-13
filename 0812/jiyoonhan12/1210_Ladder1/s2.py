import sys
sys.stdin = open('input.txt')

for T in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 시작점 초기화
    i = 99
    j = arr[99].index(2)

    while i > 0:
        i -= 1
        if j > 0 and arr[i][j-1] == 1: # 왼쪽에 1 있고
            while j > 0 and arr[i][j-1] == 1: # 칸을 벗어나거나 옆에 칸이 1이 아닐 때까지
                j -= 1 # 왼쪽으로 이동
        elif j < 99 and arr[i][j+1] == 1: # 오른쪽 동일
            while j < 99 and arr[i][j+1] == 1:
                j += 1

    print('#{} {}'.format(t, j))