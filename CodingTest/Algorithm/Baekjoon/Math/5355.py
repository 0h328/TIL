import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    info = list(map(str, input().split()))
    answer = 0
    for i in range(len(info)):
        if i == 0:
            answer += float(info[i])
        else:
            if info[i] == "#":
                answer -= 7
            elif info[i] == "%":
                answer += 5
            elif info[i] == "@":
                answer *= 3

    print("%0.2f" % answer)