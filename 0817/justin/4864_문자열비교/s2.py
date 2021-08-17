import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    pattern = input()
    target = input()
    P = len(pattern)
    T = len(target)
    count = 0                         # 같은 문자열의 개수
    idx = 0                           # 문자열 비교 idx

    for i in range(P):                # pattern의 길이만큼 반복
        check_chr = pattern[i]
        for j in range(idx, T):
            idx += 1
            if check_chr == target[j]:# idx, T-1까지 check
                count += 1
                break
        else:                         # break를 한번도 만나지 않았다는 건? 연속되는 문자가 없었다는 의미
            ans = 0                   # 0 초기화
    if count == len(pattern):
        ans = 1
    print('#{} {}'.format(tc, ans))