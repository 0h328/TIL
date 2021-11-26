import sys
sys.stdin = open('input.txt', encoding='UTF8')

for tc in range(10):
    test = int(input())
    find_word = input()
    sentence = input()

    length = sentence.count(find_word[0])

    cnt = 0
    # i = 0
    for _ in range(length):
        if sentence.find(find_word) == -1:
            break
        else:
            cnt += 1
            # i = sentence.find(find_word)
            sentence = sentence.replace(find_word, 'ZZ', 1)
            # print(sentence)
    print('#{} {}'.format(tc+1,cnt))
