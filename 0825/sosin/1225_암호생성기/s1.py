import sys
sys.stdin = open('input.txt')

from collections import deque

def sol(q):
    while True:
        for i in range(1, 6):
            temp = q.popleft()-i
            if temp <= 0:
                return list(q)+[0]
            q.append(temp)
            
for T in range(1, 11):
    input()
    arr = list(map(int, input().split()))
    for i in range(8):
        arr[i]%=120
    print('#{}'.format(T), *sol(deque(arr)))

#1 6 2 2 9 4 1 3 0 
#2 9 7 9 5 4 3 8 0 
#3 8 7 1 6 4 3 5 0 
#4 7 5 8 4 8 1 3 0 
#5 3 8 7 4 4 7 4 0 
#6 6 7 5 9 6 8 5 0 
#7 7 6 8 3 2 5 6 0 
#8 9 2 1 7 3 6 3 0 
#9 4 7 8 1 2 8 4 0 
#10 6 8 9 5 8 5 2 0 
