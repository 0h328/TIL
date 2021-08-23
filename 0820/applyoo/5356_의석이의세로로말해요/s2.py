import sys
sys.stdin = open('input.txt')


T = int(input())
for test in range(T):
    result = ''

    word = [list(input()) for _ in range(5)]

    for j in range(15):  # 최대 길이만큼 반복(열)
        for i in range(15):  # 최대 길이만큼 반복(행)
            try:
                result += word[i][j]
            except IndexError:
                pass

    print('#{} {}'.format(test+1, result))
