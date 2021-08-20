import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    box = [''.join(input().split()) for _ in range(N)]          # 가로 글자 찾기 -> 내부 요소 문자
    rotated_box = [''.join(char) for char in list(zip(*box))]   # 전치 -> 세로 글자 찾기
    ans = 0                         # 개수 카운트 변수 초기화
    target = '1' * K                # 찾아야 하는 문자열
    for check in box:
        pattern = check.split('0')  # 가로 글자 체크
        for num in pattern:
            if num == target:       # .count도 가능
                ans += 1

    for check in rotated_box:       # 세로 글자 체크
        pattern = check.split('0')
        for num in pattern:
            if num == target:
                ans += 1
    print('#{} {}'.format(tc, ans))
