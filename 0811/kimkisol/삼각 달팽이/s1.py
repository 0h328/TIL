import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution(n):
    result = []
    row = -1
    col = 0
    num = 0
    for i in range(1, n+1):
        result.append([0] * i)
    for i in range(n):
        if i % 3 == 0:
            for _ in range(n - i):
                num += 1
                row += 1
                result[row][col] = num
        elif i % 3 == 1:
            for _ in range(n - i):
                num += 1
                col += 1
                result[row][col] = num
        else:
            for _ in range(n - i):
                num += 1
                row -= 1
                col -= 1
                result[row][col] = num
    answer = sum(result, [])

    return answer

for _ in range(3):
    print(solution(int(input())))