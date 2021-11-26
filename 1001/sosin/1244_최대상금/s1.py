import sys
sys.stdin = open('input.txt')

def find_sol(s, first):
    if not s:
        return False

    max_val = max(s)
    if s[0] == max_val:
        result = find_sol(s[1:], False)
        if result:
            return [s[0]] + result
        else:
            if not first:
                return False
            s[-1], s[-2] = s[-2], s[-1]
            return s
    else:
        # 차선책, 최선책순서를 생각해야함 max value가 여러개가 있고 교환횟수도 더 남았을 시, 교환횟수 +1까지 변경해야함
        for i in range(len(s)-1, -1, -1):
            if max_val == s[i]:
                s[i], s[0] = s[0], s[i]
        return s

for T in range(int(input())):
    s, K = input().split()
    s = list(map(int, s))
    for _ in range(int(K)):
        s = find_sol(s, True)

    print('#{} {}'.format((T+1), ''.join(map(str, s))))

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645