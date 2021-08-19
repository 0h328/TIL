# 파스칼의 3각형
# 크기가 N인 파스칼의 삼각형 만들기
import sys
sys.stdin = open('input.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    result = [[1], [1, 1]]
    for i in range(2, N):
        pascal = []
        for j in range(i + 1):
            if j == 0 or j == i:
                pascal.append(1)
            else:
                pascal.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(pascal)

    print('#{}'.format(test_case))
    for i in range(N):
        for j in range(i + 1):
            print(result[i][j], end=' ')
        print()




