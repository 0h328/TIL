import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    ans = 0
    A, B = input().split()

    while True:
        before = len(A)     # 변경 전 A 길이
        A = A.replace(B, '', 1)     # B를 A에서 제거
        after = len(A)      # 변경 후 A 길이
        if before == after: # 변경 전후 길이 변화 없으면, 더이상 B 없으므로 break
            break
        ans += 1    # 길이 변화있으면 ans += 1

    ans += len(A)   # B를 전부 바꾸고 남은 글자 수를 더함

    print('#{} {}'.format(tc, ans))