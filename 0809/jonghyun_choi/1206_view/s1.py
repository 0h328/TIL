import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())
    building = list(map(int,input().split()))
    total = 0
    number = 0
    while number < N:
        if number >= 2 and number <= N-3:
            comparison = [building[index] for index in range(number-2,number+3)]
            if max(comparison) == building[number]:
                comparison.remove(building[number])
                total += building[number] - max(comparison)
        elif number == 0:
            comparison = [building[index] for index in range(number,number+3)]
            if max(comparison) == building[number]:
                comparison.remove(building[number])
                total += building[number] - max(comparison)
        elif number == 1:
            comparison = [building[index] for index in range(number-1, number+3)]
            if max(comparison) == building[number]:
                comparison.remove(building[number])
                total += building[number] - max(comparison)
        elif number == N-2:
            comparison = [building[index] for index in range(number-2, number+2)]
            if max(comparison) == building[number]:
                comparison.remove(building[number])
                total += building[number] - max(comparison)
        elif number == N-1:
            comparison = [building[index] for index in range(number-2, number+1)]
            if max(comparison) == building[number]:
                comparison.remove(building[number])
                total += building[number] - max(comparison)
        number += 1
    print('#{} {}'.format(i+1,total))



