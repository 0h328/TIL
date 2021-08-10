import sys

sys.stdin = open('input.txt')

T = int(input())


def BubbleSort(a):  # 버블정렬
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


for test in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    result = []
    for i in range(M - 1, len(data)):        # M-1 번째 인덱스 부터 하나씩 증가시키면서
        msum = 0
        for j in range(M):                   # 아래로 묶음 만큼 msum에 더한다.
            msum += data[i - j]
        result.append(msum)                  # 이값들로 리스트를 만든 후에

    BubbleSort(result)                       # 정렬하고
    answer = result[-1] - result[0]          # 가장 앞의 수와 뒤의 수를 뺀 차를

    print('#{} {}'.format(test + 1, answer)) # 프린트
