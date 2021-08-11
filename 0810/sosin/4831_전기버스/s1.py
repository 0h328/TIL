import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    # k=1회충전시 최대거리, n=종점, m=충전기 설치된 정류장 개수
    k, n, m = map(int,input().split())
    # 0, n 추가 이유는 아래에
    s_oil = [0] + list(map(int, input().split())) + [n]
    
    result = 0
    # 시작점부터, 마지막까지 갈 수 있는지 체크
    for i, s in enumerate(s_oil[:-1]):
        if s + k < s_oil[i+1]:
            break
    else:
        # 최소 충전횟수
        now_pos = 0
        while now_pos < n:
            for i in range(k, 0, -1):
                if now_pos+i in s_oil:
                    now_pos += i
                    result+=1
                    break
        result -= 1
        
    print('#{} {}'.format((T+1), result))

#1 3
#2 0
#3 4