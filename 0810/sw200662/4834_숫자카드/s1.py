import sys
sys.stdin = open('input.txt')

T = int(input()) # TEST 케이스의 숫자 가져오기

for i in range(T):
    N = int(input())                          # 카드 장수 받아오기
    Numbers = int(input())                    # 받아온 숫자 카드 저장
    cnt = [0] * 10                            # 카운팅정렬에서 아이디어를 가져와서 0~9에서 숫자니 10을 곱함
    ans = 0                                   # 가장 큰 수가 무엇인지
    max_cardnumber = 0                        # CARD숫자가 가장 많은것 저장

    while Numbers > 0:                        # 카운팅 정렬에서 아이디어를 가져와서 나머지를 각각의 cnt에 저장
        cnt[Numbers%10] += 1
        Numbers //= 10

    for Cardnumber in range(len(cnt)):        # 0~9 까지의 숫자를 다 할것이기 때문에 len(cnt)활용 < 10 해도 무방
        if cnt[Cardnumber] >= max_cardnumber: # >가 아닌 >= 한이유는 같은갯수면 더 높은 숫자를 출력하라고 해서 입력
            max_cardnumber = cnt[Cardnumber]  # max_cardnumber에 장수를 저장
            ans = Cardnumber                  # ans에 실제로 가장 큰 숫자를 저장

    print('#{} {} {}'.format(i+1,ans,max_cardnumber))
