import sys

sys.stdin = open('input.txt')

for test in range(int(input())):
    N = int(input())

    print('#{}'.format(test + 1))

    answer = []
    data =  [1]
    for i in range(N):
        data = [0]+data+[0]
        answer = [str(data[j]+data[j+1]) for j in range(i+1)]
        print(' '.join(answer))
        data = [int(h) for h in answer]