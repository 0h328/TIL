import sys
sys.stdin = open('input.txt')

#1. 행 우선 순회
def max_total_i():
    max_total_i = 0
    for i in range(100): #100개의 행
        total_i = 0
        for j in range(100):    #100개의 열
            total_i += arr[i][j]        #j가 변하니깐, 행의 합이 담긴 것
        if total_i > max_total_i :      #for 끝나면, 한행의 합이 total_i에 담긴 것.
            max_total_i = total_i       #비교해서 더 크면 max_total_i에 대입해서 바꿔 줌
    return max_total_i

#2. 열 우선 순회
def max_total_j():
    max_total_j = 0
    for j in range(100):
        total_j = 0
        for i in range(100):
            total_j += arr[i][j]
        if total_j > max_total_j:
            max_total_j = total_j
    return max_total_j

#3. 대각선 순회 (오른쪽 아래 방향)
def max_total_x():
    max_total_x = 0
    for i in range(100):
        max_total_x += arr[i][i]
    return max_total_x

#4. 대각선 순회 (오른쪽 위 방향)
def max_total_y():
    max_total_y = 0
    for i in range(100):
        max_total_y += arr[i][99-i]
    return max_total_y


for _ in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    ans = max(max_total_i(), max_total_j(), max_total_x(), max_total_y())

    print('#{} {}'.format(N, ans))