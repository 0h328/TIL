import sys
sys.stdin = open('input.txt')

delta = [-2,-1,1,2]

for case in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    res = 0
    for i in range(2, len(data) - 2):
        current_value = data[i]
        val = 0
        for k in range(4):
            if data[i + delta[k]] > val:
                val = data[i + delta[k]]

        if current_value > val:
            res += (current_value - val)

    print('#{} {}'.format(case + 1, res))
