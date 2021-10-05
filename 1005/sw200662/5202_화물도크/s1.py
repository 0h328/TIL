import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    start_list = []
    end_list = []
    start_time = 0
    ans = 0
    for i in range(N):
        s,e = map(int,input().split())
        start_list.append(s)
        end_list.append(e)
#    end_time = min(end_list)
#    end_idx = end_list.index(end_time)
    for k in range(N):
        end_idx = end_list.index(min(end_list))
        if start_time <= start_list[end_idx]:
            start_time = end_list[end_idx]
            ans += 1
        start_list.pop(end_idx)
        end_list.pop(end_idx)
    print('#{} {}'.format(tc,ans))


