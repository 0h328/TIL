import sys
sys.stdin = open('input.txt')


'''
총 소요시간 2시간 1분
thought process: 6분
머지소팅 알고리즘을 구현하는데, 순열 알고리즘을 접목 시켜야한다
머지소팅:
part1. 가운데를 기준으로 리스트 반으로 쪼갠다. => 마지막까지 무한 반복
part2. 하나하나 비교하며 합치길 반복한다
문제가 뭘 물어보는지 모르겠다. 일단 머지sorting만 구현 성공



알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.



정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.

5<=N<=1,000,000, 0 <= ai <= 1,000,000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.
'''

def merge(left, right):
    ans = []
    l = r = 0                               # 왼쪽 포인터, 오른쪽 포인터

    while l < len(left) and r < len(right):      # 포인터가 리스트를 벗어나지 않을때
        if left[l] < right[r]:              # left와 right 리스트 원소 차례대로 비교해서 작은 순으로
            ans.append(left[l])              # ans 에 반영
            l += 1
        else:
            ans.append(right[r])
            r += 1
    ans += left[l:]
    ans += right[r:]
    return ans


def cut(arr):
    if len(arr) == 1:
        return arr
    else:
        m = len(arr) // 2
        left = cut(arr[:m])
        right = cut(arr[m:])
        complete = merge(left, right)

    return complete     # 원리: 머지함수로 정렬된 complete변수가 리턴되면 left 혹은 right에 할당된다!


for tc in range(1, int(input())+1):

    N = int(input())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(tc, cut(nums)))
