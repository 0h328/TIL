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

    for i in range(max_len):
        for j in range(5):
            # 허락받고 쓰자.
            # if len(word[j]) > i:
            #     print(word[j][i], end='')
            # 허락보다 용서받는게 쉽다
            try:
                print(word[j][i], end='')
            except:
                pass
    print()