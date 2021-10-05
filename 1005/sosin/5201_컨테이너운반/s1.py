import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    result = 0
    input()
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    for truck in trucks:
        for k in range(truck):
            try:
                idx = weights.index(truck-k)
                result+=weights.pop(idx)
                break
            except:
                pass

    print('#{} {}'.format((T+1), result))

#1 8
#2 45
#3 84