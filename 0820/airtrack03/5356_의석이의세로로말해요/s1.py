import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = [input() for _ in range(5)]
    ans = ''
    # 각 줄의 길이는 1이상 15이하
    # col이 문자열 범위 넘어가는 경우 에러 발생할 것이므로 except 처리
    for col in range(15):
        for row in range(5):
            try:
                ans += data[row][col]
            except:
                continue

    print('#{} {}'.format(tc, ans))