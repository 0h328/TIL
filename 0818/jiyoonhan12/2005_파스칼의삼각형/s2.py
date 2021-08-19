import sys
sys.stdin = open('input.txt')

T = int(input())

def pascal(n):
    stack = [1, 1]
    if n > 2:
        stack.append()

for t in range(1, T + 1):
    n = int(input())
    # n이면 n줄 출력
    # 1, 2 일때는 1
    # n에 들어가는 숫자 배열 1 1+2  ... n ... 1+2 1

    # stack으로 어떻게 풀 지 모르겠어요...