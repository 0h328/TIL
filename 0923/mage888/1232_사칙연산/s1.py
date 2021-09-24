import sys
sys.stdin = open('input.txt')

def operator(k):
    if k:
        operator(left[k])
        operator(right[k])
        if op[k] == '-':
            op[k] = op[left[k]] - op[right[k]]
        elif op[k] == '+':
            op[k] = op[left[k]] + op[right[k]]
        elif op[k] == '*':
            op[k] = op[left[k]] * op[right[k]]
        elif op[k] == '/':
            op[k] = op[left[k]] / op[right[k]]

T = 10
for tc in range(1, T+1):
    N = int(input())
    op = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N):
        data = input().split()
        if len(data) == 4:
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])
            op[int(data[0])] = data[1]
        else:
            op[int(data[0])] = int(data[1])

    operator(1)
    print('#{} {}'.format(tc, int(op[1])))