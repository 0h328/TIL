import sys
sys.stdin = open('input.txt')

T = int(input())

def min_max(a):
    max_num = min_num = a[0]            # 초기값은 리스트의 첫번째 값으로 할당
    for num in a:                       # 최댓값 저장
        if num > max_num:
            max_num = num

        if num < min_num:               # 최솟값 저장
            min_num = num
    diff = max_num - min_num            # 차이 저장
    return diff

for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    ans = min_max(a)
    print('#{} {}'.format(tc, ans))
