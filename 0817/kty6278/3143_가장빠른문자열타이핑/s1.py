import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    cnt_word, word = input().split()
    # print(cnt_word, word)


    cnt = cnt_word.count(word)
    new_word = cnt_word.replace(word, '')
    # print(new_word)
    cnt += len(new_word)
    print('#{} {}'.format(tc + 1, cnt))