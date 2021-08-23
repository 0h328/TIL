import sys
sys.stdin = open('input.txt', encoding='UTF8')

for tc in range(1, 11):
    T = int(input())
    want_str = input()
    find_str = input()

    cnt = 0

    # for i in range(len(find_str) - 1):
    for i in range(len(find_str) - len(want_str) + 1):
        if find_str[i:i+len(want_str)] == want_str:
            cnt += 1
    print('#{0} {1}'.format(tc, cnt))
