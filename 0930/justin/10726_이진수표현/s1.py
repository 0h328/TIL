import sys
sys.stdin = open('input.txt')
T = int(input())
ans = ['OFF', 'ON']
result = []
for tc in range(1, T+1):
    N, M = map(int, input().split())    # M의 이진수 표현의 마지막 N번 비트가 모두 1로 켜져있는지 확인
    check = 1                           # ans의 index 1 -> ON
    for i in range(N):
        if M & (1 << i) == 0:           # i번 비트가 1인 값을 M과 &(AND) 연산하여 하나라도 0이 있다면
            check = 0                   # 0으로 변경 후 종료 (ans의 index 0 -> OFF)
            break
    result.append('#{} {}'.format(tc, ans[check]))
print('\n'.join(map(str, result)))