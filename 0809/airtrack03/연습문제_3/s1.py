import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    # 낙차의 최대값은 각 상자기둥의 가장 위 상자에서 도출
    for i in range(0, N-1):
        cnt = 0
        for j in range(i+1, N):
            if data[i] > data[j]:
                cnt += 1
        if cnt > ans:
            ans = cnt

    print('#{} {}'.format(tc, ans))