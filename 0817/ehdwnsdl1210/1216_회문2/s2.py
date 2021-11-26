import sys
sys.stdin = open('input.txt')

def find_pal():
    # 모든 행에 대해서
    for row in range(100):
        for j in range(50):
            if arr[row][j] != arr[row][100-j-1]:
                break

        else:   # 회문인 경우
            result = ''
            for k in range(j, j+50):
                result += arr[row][k]
            return result

    # 모든 열에 대해서
    for col in range(100):
        for j in range(50):
            if arr2[j][col] != arr2[100-j-1][col]:
                break

        else:   # 회문인 경우
            result = ''
            for k in range(j, j+50):
                result += arr2[k][col]
            return result

for _ in range(1, 11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))

    print('#{} {}'.format(T, find_pal()))