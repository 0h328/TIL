import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    pattern = input()
    target = input()
    ans = int(pattern in target)
    print('#{} {}'.format(tc, ans))