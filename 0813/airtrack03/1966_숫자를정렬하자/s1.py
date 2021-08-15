import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 숫자열 길이
    data = list(map(int, input().split()))
    data.sort()

    print('#{} {}'.format(tc, ' '.join(map(str, data))))