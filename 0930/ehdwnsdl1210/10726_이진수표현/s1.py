'''
정수 N, M 이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력

첫 번째 줄에 정수 N, M이 주어진다. (1 ≤ N ≤ 30 , 0 ≤ M ≤ 108)
각 테스트 케이스마다 한 줄씩
마지막 N개의 비트가 모두 켜져 있다면 ON
아니면 OFF 를 출력하라.
'''

def check_on_off(N, M):
    for j in range(N-1, -1, -1):    # N = 0 일때 그자리 1칸이라고 보면 됨 N=4 / 1000 100 10 1
        if M & (1 << j) == 0:       # N-1 부터 쭉 1이어야 통과
            return 'OFF'

    return 'ON'

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, check_on_off(N, M)))

#1 OFF
#2 OFF
#3 ON
#4 ON
#5 OFF