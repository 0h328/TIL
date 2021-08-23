import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = [0] * 5

    max_len = 0

    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])

    print('#{}'.format(tc), end=' ')

    for i in range(15):
        for j in range(5):
            # 허락받고 쓰자
            # if len(word[j]) > i:
            #     print(word[j][i], end='')
            # 일단하고 용서를 구하자
            try:
                print(word[j][i], end='')
            except:
                pass