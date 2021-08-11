import pathlib, sys
sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + '/input.txt')

for T in range(int(input())):
    counters = [0] * 10
    N = int(input())
    for i in input():
        counters[int(i)]+=1
    max_value = 0
    max_count = 0
    for i, c in enumerate(counters):
        if max_count <= c:
            max_value = i
            max_count = c

    print('#{} {} {}'.format((T+1), max_value, max_count))

#1 9 2
#2 8 1
#3 7 3