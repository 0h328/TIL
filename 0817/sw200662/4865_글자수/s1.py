import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    find_str = input()
    found_str = input()
    ans = 0
    for z in find_str:
        cnt = 0
        for k in found_str:
            if z == k:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print('#{} {}'.format(i + 1, ans))
