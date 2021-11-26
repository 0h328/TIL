import sys
sys.stdin = open("input.txt")

tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    number_list = list(map(int, input().split()))
    max_number = min(number_list)
    min_number = sum(number_list)

    for outer in range(len(number_list) - m + 1):
        compare = 0
        for inner in range(m):
            compare += number_list[outer + inner]

        if max_number < compare:
            max_number = compare

        if min_number > compare:
            min_number = compare
    result = max_number - min_number
    print("#{0} {1}".format(t, result))