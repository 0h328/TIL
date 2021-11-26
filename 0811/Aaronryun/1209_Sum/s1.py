import sys

sys.stdin = open('input.txt')

for _ in range(10):
    test = int(input())

    data = [list(map(int, input().split())) for _ in range(100)]

    result1 = []  # 행우선 합들을 저장
    for i in range(len(data)):
        msum1 = 0
        for j in data[i]:
            msum1 += j
        result1.append(msum1)

    for i in range(1, len(result1)):  # 행우선 합의 최댓값 찾기
        if result1[i] < result1[i - 1]:
            result1[i], result1[i - 1] = result1[i - 1], result1[i]
    max1 = result1[-1]

    result2 = []  # 열 우선 합들을 저장
    for i in range(len(data)):
        msum2 = 0
        for j in range(len(data[i])):
            msum2 += data[j][i]
        result2.append(msum2)

    for i in range(1, len(result2)):  # 열 우선 합의 최대값 찾기
        if result2[i] < result2[i - 1]:
            result2[i], result2[i - 1] = result2[i - 1], result2[i]
    max2 = result2[-1]

    msum3 = 0  # 오른 아래로 대각선 합
    for i in range(len(data)):
        msum3 += data[i][i]
    msum4 = 0  # 왼쪽 아래로 대각선 합
    for i in range(len(data)):
        msum4 += data[i][len(data) - (i + 1)]

    if msum3 > msum4:  # 대소 비교
        max3 = msum3
    elif msum3 < msum4:
        max3 = msum4

    final = [max1, max2, max3]  # 합들의 리스트 중에서 최대값 찾기
    for i in range(1, len(final)):
        if final[i] < final[i - 1]:
            final[i], final[i - 1] = final[i - 1], final[i]

    print('#{} {}'.format(test, final[-1]))
