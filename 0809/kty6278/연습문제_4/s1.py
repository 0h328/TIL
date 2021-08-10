import sys
sys.stdin = open('input.txt')

testcase = int(input())
for i in range(testcase):
    nums = list(map(int, input().split()))
    print(nums