def solve(rewards):
    for _ in range(int(cnt)):                        # 최대 교환 횟수 반복(필수)
        updated_reward = set()                       # 업데이트 된 set 만들어 놓고
        for reward in rewards:                       # 숫자 카드 한 세트씩 꺼내서
            tmp = list(reward)                       # 리스트로 만들고
            for i in range(len(cards)):              # 카드 길이만큼 반복 돌리며
                for j in range(i+1, len(cards)):     # i부터 i+1 ~ 끝까지 전부 교환하며 업데이트
                    tmp[i], tmp[j] = tmp[j], tmp[i]  # 바꾸고
                    updated_reward.add(''.join(tmp)) # 넣고(set이기 때문에 중복은 알아서 제거)
                    tmp[i], tmp[j] = tmp[j], tmp[i]  # 원복
        rewards = set(updated_reward)
    return max(map(int, rewards))

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    cards, cnt = input().split()        # 숫자 카드, 최대 교환 횟수
    rewards = {cards}                   # 중복 제거를 위해 set 활용
    ans = solve(rewards)
    print('#{} {}'.format(tc, ans))