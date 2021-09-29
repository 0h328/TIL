import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    person = sorted(list(map(int, input().split())))
    result = 'Possible'

    for i in range(N):
        cnt = (person[i] // M) * K
        bread = cnt - (i + 1)
        if bread < 0: # 음수가 나오는 경우 현재 i에게 판매 불가
            result = 'Impossible'
            break
    print('#{} {}'.format(tc+1, result))