import sys
sys.stdin = open('input.txt')

N = int(input())
crane = sorted(tuple(map(int, sys.stdin.readline().split())), key=lambda x: -x)
M = int(input())
box = sorted(tuple(map(int, sys.stdin.readline().split())), key=lambda x: -x)

cnt = 0

if max(crane) < max(box):   # 크레인의 무게보다 박스의 무게가 더 크면
    print(-1)               # 못 옮기므로 -1
    exit()
else:
    while box:              # 박스를 다 옮길때까지
        for c in crane:
            if box and c >= box[-1]:    # 박스가 있으면서 남은 박스의 무게보다 크레인의 무게가 크거나 같으면
                for i in range(M):      # 박스의 개수만큼 반복을 돌면서
                    if c >= box[i]:     # 크레인이 박스의 무게보다 크거나 같으면
                        box.pop(i)      # 박스를 옮기고(pop)
                        break           # break
        cnt += 1                        # 횟수 +1

print(cnt)
