import sys
sys.stdin = open('input.txt')

def partition(start, end):  # first와 end는 인덱스 값이 아닌 순서
    if start == end: # 카드 한개남는 경우
        return start
    else:
        first = partition(start, (start + end)//2)
        last = partition((start + end)//2 + 1, end)
        return winner(first, last)

def winner(first, last):  # first, last를 인덱스로 처리해주기 위해서 1씩 마이너스
    if ((numbers[first-1] == 1 and numbers[last-1] == 1) or        # 같은 값인 1인경우 - 가위
            (numbers[first-1] == 1 and numbers[last-1] == 3) or    # 다른 값인 가위 vs 보
            (numbers[first-1] == 2 and numbers[last-1] == 2) or    # 같은 값인 2인경우 - 바위
            (numbers[first-1] == 2 and numbers[last-1] == 1) or    # 다른 값인 바위 vs 가위
            (numbers[first-1] == 3 and numbers[last-1] == 3) or    # 같은 값인 3인경우 - 보
            (numbers[first-1] == 3 and numbers[last-1] == 2)):     # 다른 값인 보 vs 바위
        return first  # 위 조건의 경우 first 승리
    return last # 이외 last 승리

for tc in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))

    print('#{} {}'.format(tc+1, partition(1, N)))
