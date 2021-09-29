'''
각 테스트 케이스의 첫 줄에는 각 케이스의 트리가 갖는 정점의 총 수 N(1≤N≤100)이 주어진다. 그 다음 N줄에 걸쳐 각각의 정점 정보가 주어진다.

해당 정점에 대한 정보는 해당 정점의 알파벳, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호가 차례대로 주어진다.

정점번호는 1부터 N까지의 정수로 구분된다. 입력에서 정점 번호를 매기는 규칙은 위와 같으며, 루트 정점의 번호는 반드시 1이다.

입력에서 이웃한 알파벳이나 자식 정점의 번호는 모두 공백으로 구분된다.

위의 예시에서, 알파벳 S가 7번 정점에 해당하면 “7 S”으로 주어지고,
알파벳 ‘F’가 2번 정점에 해당하면 두 자식이 각각 알파벳 ‘O’인 4번 정점과 알파벳 ‘T’인 5번 정점이므로 “2 F 4 5”로 주어진다.

총 10개의 테스트 케이스가 주어진다,
'''

import sys
sys.stdin = open('input.txt')

def in_order(s):
    if s <= N:
        in_order(2*s)
        print('{}'.format(word[s]), end='')
        in_order(2*s+1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    word = [0] * (N+1)

    for i in range(N):
        data = input().split()
        word[i+1] = data[1]
    print(word)

    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()


