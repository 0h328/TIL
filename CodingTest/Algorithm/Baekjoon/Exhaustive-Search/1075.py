import sys
sys.stdin = open('input.txt')

N = input()
F = int(input())
ans = int(N[:-2] + '00')
while True:
    if ans % F == 0:
        break
    ans += 1
    
print(str(ans)[-2:])