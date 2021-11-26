#1.

import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc = input()
    data = [input() for _ in range(100)]
    ans = 0
    for L in range(100, 0, -1):        # 최대 길이(100)부터 마지막(1)까지 거꾸로(-1)
        for c in range(100):
            for r in range(100-L+1):   # 최대 길이부터 하나씩 줄여가면서 회문 체크
                for l in range(L//2):  # 행 체크
                    if data[c][r+l] != data[c][r+L-1-l]: # 회문이 아닌 경우
                        break                            # 종료
                else:                                    # 회문인 경우
                    ans = L                              # 길이 저장

                for l in range(L//2):                    # 열 체크 (행의 반대)
                    if data[r+l][c] != data[r+L-1-l][c]: # 회문이 아닌 경우
                        break                            # 종료
                else:                                    # 회문인 경우
                    ans = L                              # 길이 저장
            if ans:                                      # 0이 아닌 경우 -> 회문인 경우 -> 반복 종료
                break
        if ans:                                          # 0이 아닌 경우 -> 회문인 경우 -> 반복 종료
            break
    print('#{} {}'.format(tc, ans))

"""
Point
1. 큰 -> 작은 순서로 내려가기 위해서 어떻게 코드를 설계 할 것인가?
2. 반복문의 break는 바로 위의 반복문만 빠져나온다. 
 - 만약 완전 반복을 끝내고 싶으면 break를 써서 상위의 반복문을 빠져나와야 한다. 
3. r+length-1-l 일반항 잡기 
 - 행 우선 탐색의 경우 슬라이싱을 활용할 수 있지만 열 우선 탐색에서 활용 불가 
"""