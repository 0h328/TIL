import sys
sys.stdin = open('input.txt')

for tc in range(10):
    test = int(input())
    word = []
    for _ in range(100):
        word.append(input())
    # print(word)

    # 행을 기준으로 출력
    result = []
    for word_length in range(1, 101): # 단어의 길이가 가능한 함수
        for i in range(100):
            for j in range(100 - word_length + 1):
                if word[i][j:j + word_length] == word[i][j:j + word_length][::-1]:
                    result.append(word[i][j:j + word_length])
        # print(result)

        for i in range(100):
            for j in range(100 - word_length + 1):
                new_word = []
                for k in range(word_length):
                    new_word.append(word[k+j][i])
                # print(new_word)

                if new_word == new_word[::-1]:
                    final = ''.join(new_word)
                    result.append(final)
        # print(result)


    max_length = 0
    for i in range(len(result)):
        if len(result[i]) >= max_length:
            max_length = len(result[i])
    # print(max_length)


    print('#{} {}'.format(tc + 1, max_length))
