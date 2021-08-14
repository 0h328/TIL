import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

T = int(input())
#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(T):
    N = int(input())
    nums = []
    result = 0

    for n in range(N):
        nums.append(list(map(int, input().split())))

    for row in range(N):
        for col in range(N):
            for idx in range(4):
                del_row = row + dr[idx]
                del_col = col + dc[idx]
                if 0 <= del_row < N and 0 <= del_col < N:
                    result += abs(nums[row][col] - nums[del_row][del_col])

    print(result)



