import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    nums, times = input().split()
    times = int(times)
    case = set([nums])                          # 모든 경우의 수
    temp = set()                                # 한 턴 돌 때 모든 경우의 수
    for _ in range(times):
        while case:
            l = list(case.pop())                # 맨 앞에서부터 하나씩 뽑아서 다 바꿀 거임
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)):
                    l[i], l[j] = l[j], l[i]
                    temp.add(''.join(l))
                    l[i], l[j] = l[j], l[i]
        case, temp = temp, case                 # 한 턴 끝날 때마다 case 업데이트

    print('#{} {}'.format(t, max(map(int, case))))