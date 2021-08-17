import sys
sys.stdin = open('input.txt')

for tc in range(10):
    num = int(input())
    word = []
    for _ in range(8):
        word.append(input())
    # print(word)

    # 행을 기준으로 출력
    result = []
    for i in range(8):
        for j in range(8 - num + 1):
            if word[i][j:j + num] == word[i][j:j + num][::-1]:
                    result.append(word[i][j:j + num])
        # print(result)

    for i in range(8):
        for j in range(8 - num + 1):
            new_word = []
            for k in range(num):
                new_word.append(word[k+j][i])
                # print(new_word)

            if new_word == new_word[::-1]:
                final = ''.join(new_word)
                result.append(final)
        # print(result)


    num_list = []
    for i in range(len(result)):
        if len(result[i]) == num:
            num_list.append(result[i])
    # print(num_list)


    print('#{} {}'.format(tc + 1, len(num_list)))
