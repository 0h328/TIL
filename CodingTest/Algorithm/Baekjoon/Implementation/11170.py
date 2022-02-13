import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = 0
    for i in range(N, M+1):
        ans += str(i).count('0')    # 문자화 시켜서 0의 개수를 세고 ans에 누적합
    print(ans)