'''
// 테스트케이스 개수, T=1
// N=4
// A1=2, A2=4, A3=7, A4=10
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    ans = -1

    # [8, 14, 20, 28, 40, 70]
    temp = []
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            temp.append(str(data[i] * data[j]))

    for i in range(len(data)-1):
        for j in range(temp[i]):
            if len(temp[i]) > 1:
                if temp[i][j] < temp[i][j+1]:



    print('#{} {}'.format(tc, ans))






