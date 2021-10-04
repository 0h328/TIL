import sys
import copy
sys.stdin = open('input.txt')


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def check(i, j, arr, visited, cores):
    wire = 0
    while s:
        for k in range(4):
            i, j = cores[s]
            ni = i + di[k]
            nj = j + dj[k]
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                visited[ni][nj] = 1
                wire += 1
                ni = i + di[k]
                nj = j + dj[k]




#cores의 좌표를 찾아 리스트로 반환하는 함수
def cores_pos(arr):
    cores = []
    #가장자리는 빼고 계산
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                cores.append((i, j))
    return cores


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = copy.deepcopy(arr)

    cores = cores_pos(arr)