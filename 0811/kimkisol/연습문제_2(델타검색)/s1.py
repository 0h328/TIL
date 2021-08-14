import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = []

for n in range(N):
    nums.append(list(map(int, input().split())))

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

r, c = 1, 1

for idx in range(4):
    print(nums[r + dr[idx]][c + dc[idx]])