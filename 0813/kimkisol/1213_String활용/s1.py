import sys
sys.stdin = open('input.txt', encoding='UTF8')

for t in range(1, 11):
    input()
    target = input()
    chars = input()
    result = 0
    for idx in range(len(chars) - len(target) + 1):
        cnt = 0
        for idx2 in range(len(target)):
            if chars[idx + idx2] != target[idx2]:
                break
            cnt += 1
        if cnt == len(target):
            result += 1

    print('#{} {}'.format(t, result))