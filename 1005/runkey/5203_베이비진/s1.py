import sys
sys.stdin = open('input.txt')

def run2(p):
    flag = 0
    for i in range(1, len(p)):
        if p[i] - p[i - 1] == 1:
            flag += 1
        elif p[i] - p[i - 1] == 0:  # 1, 2, 2, 3
            continue
        else:
            flag = 0

        if flag == 2:
            return True
    return False

def triple(p):
    flag = 0
    for i in range(1, len(p)):
        if p[i] - p[i - 1] == 0:
            flag += 1
        else:
            flag = 0

        if flag == 2:
            return True
    return False

tc = int(input())

for t in range(1, tc + 1):
    result = 0
    cnt = 1
    p_list = list(map(int, input().split()))
    p1 = []
    p2 = []
    p1_run, p1_tri, p2_run, p2_tri = 0, 0, 0, 0
    for p in p_list:
        if cnt % 2:
            p1.append(p)
            p1.sort()
            if cnt >= 5:
                p1_run = run2(p1)
                p1_tri = triple(p1)
        else:
            p2.append(p)
            p2.sort()
            if cnt >= 6:
                p2_run = run2(p2)
                p2_tri = triple(p2)
        cnt += 1
        if p1_run or p1_tri:
            result = 1
            break
        elif p2_run or p2_tri:
            result = 2
            break

    print("#{} {}".format(t, result))