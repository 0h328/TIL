import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    pascal = [[1]] + [[1]+[0]*i+[1] for i in range(0, N-1)]
    print(pascal)
    for i in range(2, N): #행
        for j in range(1, (i+1)//2 + 1):  # 열(idx 1부터 앞뒤로 하나씩)
            pascal[i][j] = pascal[i][i-j] = pascal[i-1][j-1] + pascal[i-1][j]
    #출력
    print('#{}'.format(t))
    for i in range(N):
        print(*pascal[i])
