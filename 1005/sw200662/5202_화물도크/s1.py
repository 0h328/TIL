import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    start_list = []
    end_list = []
    end_time = 0                                  # 전 화물차의의 끝나는 시간
    ans = 0

    for i in range(N):
        s,e = map(int,input().split())            # s,e를 하나씩 받아와서
        start_list.append(s)                      # s는 start리스트에
        end_list.append(e)                        # e는 end 리스트에 저장

    for k in range(N):
        end_idx = end_list.index(min(end_list))  # end_list에서 가장
        if end_time <= start_list[end_idx]:      # 만약 > 전의 끝나는 시간보다 지금 선택한 화물의 끝나는 시간이 늦으면
            end_time = end_list[end_idx]         # end_time을 선택한 화물의 끝나는시간으로 결정
            ans += 1
        start_list.pop(end_idx)                  # if문의 유무와 상관없이 start와 end에서 모두 제거
        end_list.pop(end_idx)

    print('#{} {}'.format(tc,ans))


