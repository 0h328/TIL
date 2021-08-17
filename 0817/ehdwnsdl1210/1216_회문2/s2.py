import sys
sys.stdin = open('input.txt')

def find_pal():
    # 모든 행에 대해서
    for row in range(100):
        for i in range(100 - M + 1):
            for j in range(M // 2):
                if arr[row][i+j] != arr[row][i-j+M-1]:
                    break

            else:   # 회문인 경우
                result = ''
                for k in range(i, i+M):
                    result += arr[row][k]
                return result

    # 모든 열에 대해서
    for col in range(100):
        for i in range(100 - M + 1):
            for j in range(M // 2):
                if arr[i+j][col] != arr[i-j+M-1][col]:
                    break

            else:   # 회문인 경우
                result = ''
                for k in range(i, i+M):
                    result += arr[k][col]
                return result

for _ in range(1, 11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))

    print('#{} {}'.format(T, find_pal()))