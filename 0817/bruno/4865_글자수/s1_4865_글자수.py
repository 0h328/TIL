import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    target = input()
    max_cnt = 0
    for i in range(len(word)):
        cnt = 0
        for j in range(len(target)):
            if word[i] == target[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    print('#{} {}'.format(tc, max_cnt))