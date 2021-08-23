# dp - 또보나치
def fibo_dp(num):
    # 피보나치의 하위 -> 상위 결과값이 담길 리스트(테이블) 선언
    result = [0 for _ in range(num+1)]
    # 0항과 1항 값 넣어놓기
    result[0] = 0
    result[1] = 1

    # 두 번째 항부터 시작 (0항과 1항은 미리 계산)
    for i in range(2, num+1):
        # 기존에 리스트에 저장된 값을 그대로 활용
        result[i] = result[i-2] + result[i-1]

    # 마지막 항 반환
    return result[num]

print(fibo_dp(50))