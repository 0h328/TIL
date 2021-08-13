import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
nums = []

for t in range(1, T+1):
    nums.append(list(map(int, input().split())))

print('행 우선 순회')
for i in range(T):
    for j in range(T):
        print(nums[i][j], end='\t')
    print()

print('열 우선 순회')
for i in range(T):
    for j in range(T):
        print(nums[j][i], end='\t')
    print()

print('지그재그 순회')
for i in range(T):
    for j in range(T):
        print(nums[i][j + ((i%2) * (T-1-2*j))], end='\t')
    print()

print('전치행렬')
nums2 = nums[:]
for i in range(T):
    for j in range(T):
        if i < j:
            nums2[i][j], nums2[j][i] = nums2[j][i], nums2[i][j]
        print(nums[i][j], end='\t')
    print()