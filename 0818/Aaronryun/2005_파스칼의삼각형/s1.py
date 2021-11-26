import sys

sys.stdin = open('input.txt')

for test in range(int(input())):
    N = int(input())

    answer = [[1]]
    print('#{}\n{}'.format(test + 1,1))

    for i in range(1, N):
        data = [1]
        for j in range(i - 1):
            msum = answer[-1][j+0]+answer[-1][j+1]
            data.append(msum)
        data.append(1)
        answer.append(data)
        print(*data)
    # #
    # for i in answer:
    #     print(*i)
