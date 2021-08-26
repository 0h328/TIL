import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    pw = list(map(int, input().split()))

    k = 0                               # 차감하기 위해 만든 변수
    while pw[-1] > 0:                   # pw의 마지막 idx가 0이 되면 종료
        k = (k+1) % 6                   # k가 0~5까지만 반복하기 위해 만든 식

        if k:                           # k가 0이 아닌, 1~5감소만 해야하므로
            pw.append(pw.pop(0)-k)

    if pw[-1] < 0:                      # pw의 마지막 idx가 음수가 되면
        pw[-1] = 0                      # 0으로 유지
    print('#{} {}'.format(tc, ' '.join(map(str, pw))))