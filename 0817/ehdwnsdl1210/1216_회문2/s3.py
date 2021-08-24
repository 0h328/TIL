import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))

    pal_list = []

    for l in range(1, 101):
        # 행 회문 찾기
        for i in range(100):
            for j in range(50):
                if arr[i][j:j+l] == arr[i][-j-1:-j-1-l]:
                    pal_list.append(arr[i][j:j+l])

        # 열 회문 찾기
        for i in range(100):
            for j in range(50):
                if arr2[i][j:j+l] == arr2[i][-j-1:-j-1-l]:
                    pal_list.append(''.join(arr2[i][j:j+l]))

    print('#{} {}'.format(T, pal_list))