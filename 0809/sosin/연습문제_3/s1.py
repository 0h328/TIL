import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N = int(input())
    boxes = list(map(int, input().split()))
    result = 0
    for i in range(len(boxes)-1):
        max_gravity = N-(i+1)
        if max_gravity < result:
            break

        for j in range(i+1, len(boxes)):
            if boxes[i] <= boxes[j]:
                max_gravity-=1
                if max_gravity < result:
                    break
        result = max(result, max_gravity)
    print(result)
