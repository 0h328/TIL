import sys
sys.stdin = open('input.txt')

def sol(string, cnt):
    if len(string) > 1:
        cnt += 1
        t = 0
        for i in string:
            t += int(i)
        sol(str(t), cnt)
    else:
        if int(string) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")


X = input()
cnt = 0
sol(X, cnt)
