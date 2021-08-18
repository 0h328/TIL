import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    number = int(input())
    print('#{}'.format(tc))
    if number <= 1:                                 # number가 1보다 작다면 1만을 출력
        print(1)
        continue
    pascal = [[0] * number for _ in range(number)]  # number가 1보다 크다면 빈 배열을 만들고
    pascal[0][0] = 1                                # 첫째 줄과 둘째 줄 값을 미리 입력
    pascal[1][0] = 1
    pascal[1][1] = 1
    if number == 2:                                 # number가 2이면 방금 입력한 그대로 출력
        for m in range(number):
            for n in range(number):
                if pascal[m][n] != 0:
                    print(pascal[m][n], end=' ')
            print()
    
    else:                                           # number가 2보다 크면 파스칼 삼각형을 계산해서 만들어줘야 함
        for i in range(2, number):
            for j in range(number):
                if j == 0 or j == i:                # 파스칼 삼각형의 좌우는 항상 1의 값을 가지고 있음
                    pascal[i][j] = 1
                else:                               # 양 옆이 아니라면, 윗줄에 있는 두 숫자의 합이 아랫줄의 숫자가 되도록 함
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        for k in range(number):
            for l in range(number):
                if pascal[k][l] != 0:               # 배열에서 0이 아니라면
                    print(pascal[k][l], end=' ')    # 출력
            print()