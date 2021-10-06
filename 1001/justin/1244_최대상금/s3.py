import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    data, N = input().split()                                           # 숫자(문자), 교환 횟수
    nums = [data]                                                       # DP 활용
    for _ in range(int(N)):                                             # 교환횟수
        b = nums
        a = []
        for i in range(len(data)-1):
            for j in range(i+1, len(data)):
                for number in b:
                    c = number
                    c = c[:i] + c[j] + c[i+1:j] + c[i] + c[j+1:]
                    if c not in a:
                        a.append(c)
    ans = max(map(int, a))
    print('#{} {}'.format(tc, ans))