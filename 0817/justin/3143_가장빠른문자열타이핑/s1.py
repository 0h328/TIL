import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    whole, part = input().split()                                             # 전체, 부분 문자
    # (전체 길이 - (part 문자의 수 * part의 길이)) + part의 수
    ans = (len(whole) - (whole.count(part) * len(part))) + whole.count(part)
    print('#{} {}'.format(tc, ans))