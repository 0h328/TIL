import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    for i in range(N):      # 1을 탐색하는 반복문
        if "1" in arr[i]:
            start = i
            break
    arr = arr[start : start + 7]

    end = M
    for i in range(M - 1, -1, -1):  # 암호가 1로 끝나니까 뒤에서 확인
        if arr[0][i] == "1":
            end = i
            break

    # 검증을 해야하는데