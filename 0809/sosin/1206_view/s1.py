import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, len(buildings)-2):
        temp = buildings[i]
        for j in range(-2, 3):
            if buildings[i] < buildings[i+j]:
                break
            elif i == i+j:
                continue
            else:
                temp = min(temp, buildings[i] - buildings[i+j])
        else:
            result += temp
        
    print('#{} {}'.format(T, result))
