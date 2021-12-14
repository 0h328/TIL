import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
nums = []
stack = []

now = 1
for _ in range(n):
    target = int(sys.stdin.readline().strip())
    while now <= target:
        stack.append('+')
        nums.append(now)
        now += 1
    if nums[-1] == target:
        nums.pop()
        stack.append('-')
    else:
        print('NO')
        exit()

if not nums:
    for ans in stack:
        print(ans)





