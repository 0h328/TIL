'''
90도로 회전하지 않은 상태에서 모든 막대들을 오른쪽으로 쭉 밀었을때 갈수있는 최대의 길이를 구하면 정답과 동일하다

1. 입력을 받아 리스트에 기둥의 높이 값들을 할당한다.
2. 반복문으로 리스트의 뒤에서 부터 순환한다
3. 2중 반복문으로 해당 기둥 오른쪽에 그 기둥 보다 크거나 같은 기둥이 몇개인지 카운트한다. cnt
4. 낙차 값 = 오른쪽 끝으로 부터 떨어진 거리 - cnt 를 한다.


예상 시간복잡도 O(n log n)
'''



import sys
sys.stdin = open('input.txt')


test_case = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, test_case+1):
    num = int(input())                          # 가로의 길이
    num_list = list(map(int, input().split()))  # 기둥의 높이 값들을 담은 리스트
    answer = []                                 # 각 기둥의 낙차 값을 담을 리스트

    # 기둥이 오른쪽 끝으로 옮겨져야하므로, 오른쪽 기둥부터 움직여야해서 리스트 뒤에서 부터 순환
    for i in range(num-1, -1, -1):
        cnt = 0                                 # 해당 기둥보다 높거나 같은 기둥이 몇개가 있는지 담을 변수
        for j in range(i+1, num):               # 2중 반복문으로 지금 기둥 오른쪽에 높거나 같은 기둥이 몇개인지 확인하기 위함
               if num_list[i] <= num_list[j]:   # 높거나 같은 기둥이 있다면 cnt + 1
                   cnt += 1
        answer.append((num-1)-i-cnt)            # 가로의 길이 - 현재 기둥의 위치 - 오른쪽에 나보다 크거나 같은 기둥의 갯수
                                                # 여기에서 인덱스는 0부터 num-1 까지이므로 연산에 -1을 추가한다.


    print('#{} {}'.format(tc, max(answer)))     # 출력