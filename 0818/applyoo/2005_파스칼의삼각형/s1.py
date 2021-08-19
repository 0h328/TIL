import sys
sys.stdin = open('input.txt')


def pascal(num):
    result = []

    for row in range(1, num + 1): # 기본 틀 생성
        result.append([1] * row)
    
    for i in range(1, num): # 가로 순회
        for j in range(1, len(result[i]) - 1): # 세로 순회(범위는 1 ~ 길이 - 1)
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j] # 해당 값 = 왼쪽 위 + 오른쪽 위
    return result


T = int(input())

for test in range(T):
    N = int(input())

    pascal_tri = pascal(N)
    print('#{}'.format(test+1))

    for i in range(N):
        print(*pascal_tri[i])