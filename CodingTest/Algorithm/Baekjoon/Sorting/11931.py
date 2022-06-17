import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort(reverse=True)
for num in nums:
    print(num)