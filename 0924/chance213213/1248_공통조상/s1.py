import sys
sys.stdin = open('input.txt')

def in_order(v):
    if v <= V:
        in_order(v*2)
        in_order(v*2+1)

T = int(input())

for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    nums = list(map(int, input().split()))
    trees = [[0]*2 for _ in range(V+1)]
    for i in range(E//2):
        if trees[nums[2*i]][0] == 0:
            trees[nums[2*i]][0] = nums[2*i+1]
        else:
            trees[nums[2*i]][1] = nums[2*i+1]
    trees[A]
    print(trees)
        #a = trees[nums[2*i]]
        #b = (trees[2*i+1])

