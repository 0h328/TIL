import sys
sys.stdin = open('input.txt', encoding='UTF8')

for _ in range(10):
    N = int(input())
    search_word = input()
    search_list = input()
    cnt = 0
    for i in range(len(search_list)):
        if search_list[i] == search_word[0]:
            if search_list[i:i+len(search_word)] == search_word:
                cnt += 1
    print('#{} {}'.format(N, cnt))
