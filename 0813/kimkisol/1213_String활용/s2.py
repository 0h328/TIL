import sys
sys.stdin = open('input.txt', encoding='UTF8')

for t in range(1, 11):
    input()
    target = input()
    chars = input()
    result = chars.count(target)

    print('#{} {}'.format(t, result))