import sys
sys.stdin = open('input.txt')

for test in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2:
            arrive = i           # 가장 마지막 줄에 2가 있는 위치를 arrive에 저장

    for j in range(99, -1, -1):
        if 0 <= arrive < 100:
            if (arrive-1) in range(len(arr)) and arr[j][arrive - 1]:
                while (arrive-1) in range(len(arr)) and arr[j][arrive-1] > 0:
                    arrive -= 1

            elif (arrive+1) in range(len(arr)) and arr[j][arrive + 1]:
                while (arrive-1) in range(len(arr)) and arr[j][arrive+1] > 0:
                    arrive += 1


    print(arrive)