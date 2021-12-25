import sys
sys.stdin = open('input.txt')

N = int(input())
for i in range(1, N+1): # 생성자를 찾기 위한 for문
    res = i + sum(map(int, str(i))) # 생성자+생성자 분해(각 자리수 더하기)

    if res == N:
        print(i)
        break

else:   # 다돌았는데도 안나오면 0 출력
    print(0)