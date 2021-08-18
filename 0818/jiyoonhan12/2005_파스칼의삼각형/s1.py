import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):

    num = int(input())
    arr = [[1] * n for n in range(1, num + 1)]  # 2차원 배열로 파스칼 삼각형 만들기 (기본값 1)
    for l in range(num):
        for r in range(l):
            if r == 0 or r == l: # 각 행의 첫번째와 마지막은 그대로 1
                pass
            else:
                arr[l][r] = arr[l - 1][r - 1] + arr[l - 1][r]

    print('#{}'.format(t))
    for lst in arr:  # 한 리스트씩 출력
        result = [x for x in lst]
        print(*result)