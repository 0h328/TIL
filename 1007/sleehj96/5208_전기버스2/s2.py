import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    batteries = list(map(int, input().split()))
    N = batteries.pop(0)

    ans = 0     # 교체 횟수 정답으로 출력

    while True:

        success = False
        time = 0
        curr_battery = batteries[0]
        while time < N:
            curr_battery -= 1



            time += 1



        ans += 1

    print('#{0} {1}'.format(tc+1, ans))
    # break
