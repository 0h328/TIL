import pathlib, sys
sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + '/input.txt')

for T in range(int(input())):
    max_value = 0
    min_value = 1e6
    N = int(input())
    my_numbers = map(int, input().split())
    for n in my_numbers:
        if max_value < n:
            max_value = n
        if min_value > n:
            min_value = n
    
    print('#{} {}'.format((T+1), (max_value-min_value)))

#1 630739
#2 740510
#3 838110