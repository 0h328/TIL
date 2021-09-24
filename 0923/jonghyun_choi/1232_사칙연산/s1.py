import sys
sys.stdin = open('input.txt')

def cal(num1, sign, num2):
    if sign == '+':
        return int(num1) + int(num2)
    elif sign == '-':
        return int(num1) - int(num2)
    elif sign == '*':
        return int(num1) * int(num2)
    elif sign == '/':
        return int(num1) / int(num2)


for case in range(10):
    N = int(input())
    tree = [[0] * 2 for _ in range(N + 1)]

    val = [0] * (N + 1)
    for _ in range(N):
        data = list(map(str, input().split()))
        if len(data) == 4:
            tree[int(data[0])][0] = int(data[2])
            tree[int(data[0])][1] = int(data[3])

        val[int(data[0])] = data[1]

    for i in range(N, 0, -1):
        if not val[i].isdecimal():
            val[i] = cal(val[tree[i][0]],val[i],val[tree[i][1]])

    print('#{} {}'.format(case + 1, int(val[1])))



