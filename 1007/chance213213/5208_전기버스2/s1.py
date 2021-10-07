import sys
sys.stdin = open('input.txt')

def check(idx, end, stops):
    visited = [0] * end
    #print(visited)
    #print(stops)
    while idx <= end:
    #for idx in range(1, len(stops)):
        if visited[idx] == 0 and (stops[idx-1] + stops[idx] >= end):
            return sum(visited)
        else:
            visited[idx] = 0
            idx += 1
            check(idx, end, stops)
    return sum(visited)



T = int(input())




for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    end = nums[0]
    stops = nums[1:]
    stops.insert(0, 0)
    print(check(0, end, stops))

