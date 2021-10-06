import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    times = [tuple(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    curr_time = 0
    for time in times:
        if time[0] >= curr_time:
            ans += 1
            curr_time = time[1]

    print('#{0} {1}'.format(tc+1, ans))
    # break
