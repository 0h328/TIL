import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, S = input().split()              # 자리수 N, N자리 16진수
    print('#{}'.format(tc), end=' ')

    for i in range(int(N)):
        t = int(S[i], 16)               # hex -> 16 (문자열을 16진수의 정수로 바꿈) - int의 기능 활용
        # print(t)
        for j in range(3, -1, -1):      # 16 -> 2 (3번 비트부터 0번까지 검사)
            if (t & (2 ** j)) == 0:     # j번 비트가 1인값과 비트 검사
                print(0, end='')
            else:
                print(1, end='')
    print()