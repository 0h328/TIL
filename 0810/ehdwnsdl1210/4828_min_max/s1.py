import sys
sys.stdin = open('input.txt')

n = int(input())

for a in range(n):
    m = int(input())
    k = list(map(int, input().split()))
    for i in range(len(k)-1, 0, -1):        # 버블 정렬
        for j in range(i):
            if k[j] > k[j+1]:
                k[j], k[j+1] = k[j+1], k[j]

    cal = k[-1] - k[0]      # 최대 - 최소

    print('#{} {}'.format(a+1, cal))