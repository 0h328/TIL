import sys
sys.stdin = open('input.txt', encoding='UTF8')

for _ in range(10):
    idx = int(input())
    word = input()
    target = input()
    word_idx, target_idx, cnt = 0, 0, 0

    while target_idx < len(target):
        if word[word_idx] == target[target_idx]:
            word_idx += 1
            target_idx += 1
            if word_idx >= len(word):
                cnt += 1
                word_idx = 0
        elif word_idx > 0:
            word_idx = 0
        else:
            target_idx += 1


    print('#{} {}'.format(idx, cnt))

