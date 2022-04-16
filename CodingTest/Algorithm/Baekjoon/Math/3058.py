import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))

    total = 0
    even = []
    for num in nums:
        if num % 2 == 0:
            total += num
            even.append(num)

    print(total, min(even))