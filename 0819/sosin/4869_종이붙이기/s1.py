import sys
sys.stdin = open('input.txt')

def sol(remain):
    if remain == 10:
        return 1
    elif remain == 20:
        return 3
        
    stack = [(remain-10, 1), (remain-20, 2)]
    answer = 0

    while stack:
        rm, count = stack.pop()
        if rm >= 20:
            stack.append((rm-10, count*1))
            stack.append((rm-20, count*2))
        else:
            answer += count
    return answer

for T in range(int(input())):
    result = 0
    N = int(input())
    print('#{} {}'.format((T+1), sol(N)))

#1 5
#2 21
#3 85