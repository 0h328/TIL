import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    total = 0
    tmp = 0
    for _ in range(N):
        C, G = map(float, input().split())
        total += C
        tmp += C*G
    GPA = tmp/total

    print(format(total, '.0f'), format(GPA, '.1f'))