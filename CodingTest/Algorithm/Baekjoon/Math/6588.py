import sys
sys.stdin = open('input.txt')

num = 1000001
arr = [True for _ in range(num)]
for i in range(2, int((num-1)**0.5)+1):
    if arr[i]:
        for k in range(i+i, num, i):
            arr[k] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    flag = 0

    for a in range(3, len(arr)):
        if arr[a] and arr[n-a]:
            print(str(n) + " = " + str(a) + " + " + str(n-a))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")