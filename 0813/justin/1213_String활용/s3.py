import sys
sys.stdin = open('input.txt', encoding='utf-8')
for _ in range(1, 11):
    tc = input()
    pattern = input()                  # pattern -> 찾고자 하는 문자
    target = input()                   # target -> 전체 문자
    ans = target.count(pattern)        # 전체 문제에서 pattern의 개수 구하기
    print('#{} {}'.format(tc, ans))