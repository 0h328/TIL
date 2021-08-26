from collections import deque
import sys
sys.stdin = open("input.txt")

for _ in range(10):
    num  = int(input())
    q_list = list(map(int, input().split()))
    tmp = []
    cnt = 1
    while True:
        tmp = q_list.pop(0)
        tmp -= cnt
        cnt += 1
        if cnt == 6:
            cnt = 1
        if tmp <= 0:
            tmp = 0
            break
        q_list.append(tmp)
    result = ' '.join(map(str, q_list))
    print("#{} {} 0".format(num, result))
