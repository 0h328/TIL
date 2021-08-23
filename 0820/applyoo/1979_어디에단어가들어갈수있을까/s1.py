import sys
sys.stdin = open('input.txt')


def word_position(arr, word):
    result = 0

    for i in range(len(arr)):
        row_cnt = 0 # 가로 확인
        col_cnt = 0 # 세로 확인
        for j in range(len(arr)):
            if arr[i][j] == 0: # 가로로 확인할 때, 해당 값이 0인 경우
                if row_cnt == word: # 가로 확인이 M과 동일한 경우
                    result += 1
                row_cnt = 0 # 초기화
            elif arr[i][j] == 1: # 가로로 확인할 때, 해당 값이 1인 경우
                row_cnt += 1
                if row_cnt == word and j == (len(arr) - 1): # 가로 확인이 M과 동일한데 마지막 요소인 경우
                    result += 1

            if arr[j][i] == 0:
                if col_cnt == word: # 세로로 확인할 때, 해당 값이 0인 경우
                    if col_cnt == word: # 세로 확인이 M과 동일한 경우
                        result += 1
                col_cnt = 0 # 초기화
            elif arr[j][i] == 1: # 세로로 확인할 때, 해당 값이 1인 경우
                col_cnt += 1
                if col_cnt == word and j == (len(arr) - 1): # 세로 확인이 M과 동일한데 마지막 요소인 경우
                    result += 1

    return result

T = int(input())
for test in range(T):
    N, word = list(map(int, input().split()))
    word_map = []
    for i in range(N):
        word_map.append(list(map(int, input().split())))

    print('#{}'.format(test+1), end = ' ')
    print(word_position(word_map, word))