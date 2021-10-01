import sys
sys.stdin = open('input.txt')


'''
얘도 안끝남
'''


di = [-1, 0, 1, 0]
dj = [0, 1, 0, 1]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    processor = []                                      # 연결해야 될 프로세서 위치
    for i in range(N):
        line = list(map(int, input().split()))
        arr.append(line)
        if 0 < i < N-1:
            for j in range(1, N-1):
                if line[j]:
                    processor.append((i, j))

    ans = [0, N*N]
    stack = [(0, 0, 0, arr)]
    while stack:
        i, core, wire, arr = stack.pop()
        if i == len(processor):
            if core > ans[0] or (core == ans[0] and wire <= ans[1]):
                ans = [core, wire]
        elif N - i + core > ans[0] or (N - i + core == ans[0] and wire <= ans[1]):
            stack.append((i+1, core, wire, [line[:] for line in arr]))
            for k in range(4):
                i, j = processor[i]
                i += di[k]
                j += dj[k]
                wire2 = wire
                arr2 = [line[:] for line in arr]
                while 0 <= i < N and 0 <= j < N and arr[i][j] == 0:
                    arr2[i][j] = 1
                    wire2 += 1
                    i += di[k]
                    j += dj[k]
                if i == -1 or i == N or j == -1 or j == N:
                    stack.append((i+1, core+1, wire2, arr2))
    print(ans[1])