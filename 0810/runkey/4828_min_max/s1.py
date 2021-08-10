import sys
sys.stdin = open("input.txt")

for t in range(1, int(input()) + 1):
    number = input()
    number_list = list(map(int, input().split()))
    number_max = max(number_list)
    number_min = min(number_list)
    result = number_max - number_min
    print("#{0} {1}".format(t, result))