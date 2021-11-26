import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N, M, L = map(int, input().split())

    data = [0] * (N + 1)
    for i in range(M):
        temp = list(map(int, input().split()))
        data[temp[0]] = temp[1]
    print(data)


    while N > 1:
        data[N // 2] += data[N]
        N -= 1
    print(data)

    print('#{} {}'.format(test, data[L]))


# for i in range(N - M, 0, -1):
    #     try:
    #         data[i] = data[i * 2] + data[i * 2 + 1]
    #     except:
    #         data[i] = data[i * 2]