import sys
sys.stdin = open('input.txt', encoding='UTF8')

for _ in range(10):
    idx = int(input())
    word = input()
    target = input()
    word_idx, target_idx, cnt = 0, 0, 0

    while target_idx < len(target):
        if word[word_idx] == target[target_idx]:        # 탐색 대상과 찾는 단어의 해당 위치의 문자가 같으면 아래 내용 실행
            word_idx += 1
            target_idx += 1
            if word_idx >= len(word):                   # word_idx가 len(word)-1이 되면 원하는 문자열을 찾은것이라고 판단
                cnt += 1
                word_idx = 0
        elif word_idx > 0:                              # if문을 만족하지 않고, word_idx가 0보다 크면 온전하게 한 word가 존재하는건 아님
            word_idx = 0
        else:
            target_idx += 1


    print('#{} {}'.format(idx, cnt))

