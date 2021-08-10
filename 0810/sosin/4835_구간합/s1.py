import pathlib, sys
sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + '/input.txt')

for T in range(int(input())):
    N, M = map(int, input().split())                        # N, M
    numbers = list(map(int, input().split()))               # 숫자 리스트
    max_value = 0                                           # 조건 상 최대값은 0 미만으로 내려갈 수 없음
    min_value = 1e6                                         # 조건 상 최소값은 100만 이상이 될 수 없음
    
    for i in range(len(numbers)-(M-1)):                     # 0부터 M개의 구간합을 계산할 수 있는 범위까지
        temp = sum(numbers[i:i+M])                          # 현재 구간의 합
        max_value = max(max_value, temp)                    # max_value를 최신화
        min_value = min(min_value, temp)                    # min_value를 최신화
    
    print('#{} {}'.format((T+1), (max_value-min_value)))    # max_value에서 min_value를 빼준 값을 출력

#1 21
#2 11088
#3 1090