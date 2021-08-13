import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i][4] != arr[j][4]:
                x0 = max(arr[i][1], arr[j][1])  # 겹치는 부분 사각형을 그리기 위해서 시점중의 가장 큰값
                y0 = max(arr[i][0], arr[j][0])  # 종점중에 가장 작은 값들을 뽑아 시점, 종점을 만들어낸다.
                x1 = min(arr[i][3], arr[j][3])
                y1 = min(arr[i][2], arr[j][2])
                x = x1 - x0     # 결국 새로운 시점 종점이기 때문에 두 점의 차이 가 0보다 작은경우 종점이 더 작아 겹치지 않는경우
                y = y1 - y0
                if x >= 0 and y >= 0:   # 그럼에도 0을 하는 이유는 두 시점종점이 겹치는 경우. 좌표가 아니라 같은 칸을 색칠하는경우이라서.
                    result += (x + 1) * (y + 1)

    print('#{} {}'.format(test_case, result))




