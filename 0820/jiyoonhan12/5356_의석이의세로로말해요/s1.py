import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    arr = [[] for _ in range(5)] # 5 row
    for i in range(5): # 한 줄로 쓰고 싶은데
        text = input()
        for idx in range(len(text)):
            arr[i].append(text[idx])
    res = ''
    for j in range(15): # col max: 15 / col first
        for i in range(5):
            try:
                res += arr[i][j]
            except: # 값이 없으면 pass
                pass
    print('#{} {}'.format(t, res))