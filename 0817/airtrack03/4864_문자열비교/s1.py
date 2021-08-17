import sys

sys.stdin = open('input.txt')

# T = int(sys.stdin.readline())
T = int(input())

for tc in range(1, T+1):
    # .rstrip() 안 붙여주면 pattern에 \n 들어가서 오답
    # pattern = sys.stdin.readline().rstrip()
    # target = sys.stdin.readline().rstrip()
    pattern = input()
    target = input()

    if pattern in target:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))