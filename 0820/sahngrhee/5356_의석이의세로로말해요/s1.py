import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    word = [0] * 5

    max_len = 0

    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])

    print("#{}".format(test_case), end=' ')

    for i in range(max_len):
        for j in range(5):
            # #1. 허락받고 쓰자
            # if len(word[j]) > i:
            #     print(word[j][i], end="")
            #2. 허락은 무슨 용서를 구하자...
            try:
                print(word[j][i], end='')
            except:
                pass
    print()