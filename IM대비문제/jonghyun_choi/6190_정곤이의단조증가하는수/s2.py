import sys
sys.stdin = open('input.txt')

T = int(input())

def increase(num):
    pos = ''
    for i in num:
        if not pos:
            pos += i
        elif pos[-1] <= i:
            pos += i
        else:
            pos = ''
            break
    return pos


for case in range(T):
    N = int(input())
    data = list(map(str, input().split()))
    res = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if increase(str(int(data[i]) * int(data[j]))):
                res.append(int(increase(str(int(data[i]) * int(data[j])))))
    sorted_res = sorted(res)
    if len(res) == 0:
        print('#{} {}'.format(case + 1, -1))
    else:
        print('#{} {}'.format(case + 1, int(sorted_res[-1])))