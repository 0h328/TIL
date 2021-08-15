import sys
sys.stdin = open('input.txt', encoding='UTF8')

for tc in range(1, 11):
    N = int(input())
    find_word = str(input())
    total_word = str(input())
    cnt = total_word.count(find_word)

    print('#{} {}'.format(N, cnt))