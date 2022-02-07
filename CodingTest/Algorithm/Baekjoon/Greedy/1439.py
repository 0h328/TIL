import sys
sys.stdin = open('input.txt')

S = input() # 101010101 -> 1이 5번 바뀌는 것보다 0이 4번 바뀌는게 더 빠름
cnt = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:      # 인접한 idx가 같지 않으면
        cnt += 1            # 개수를 세어준다.

print((cnt+1) // 2)         # 101010의 경우 3번 (0 or 1) 바꿔야하는데
                            # cnt는 5인 상태이므로 몫으로 나누면 2가 된다.
                            # 따라서 cnt + 1을 해줘야한다.