#1. sol
import random
import time

# 캐릭터별 대사


def character_line(name):
    global dead, kick

    if name == '피셔':
        print('피셔: 아버지를 닮지 못해 실망하셨죠?')
        print('\n', '\t'*(dream_depth-1), 'MISSION SUCCEESS\n')
        visited['피셔'] = True

    elif name == '맬':
        print('맬: 안녕? [탕!]')
        dead = True

    elif name in ['방해꾼1', '방해꾼2']:
        print('코브: 으아아아가아아앙그가앙아강악악아아아악!')
        kick = True

    elif name == '사이토':
        print('사이토: 날 죽이러 온건가....')

    elif name == '아서':
        print('아서: 코끼리를 생각하지 말라고 하면 뭘 생각할까요?')

    elif name == '임스':
        print('임스: 사나이라면 꿈을 크게 가져야지.')

# 꿈속으로


def into_dream():
    time.sleep(1)
    global dream_depth

    if kick or dead:            # 킥을 하거나 죽었을 때
        print()
        print('\t'*(dream_depth-2), 'MISSION FAILED')
        print()
        return

    if visited['피셔']:         # 피셔를 만나면
        return                  # 리턴

    idx = random.randint(0, len(characters)-1)      # 꿈 속에서 누굴 만날지에 대한 인덱스 변수
    while idx in selected:                          # 중복으로 같은 사람을 만나는 것 방지
        idx = random.randint(0, len(characters)-1)

    whom_i_have_met = characters[idx]               # 만난 사람을 인덱스로 접근
    selected.append(idx)                            # selected 스택에 그 인덱스 저장

    character_stack.append(whom_i_have_met)         # character_stack에 그 사람 저장

    if dream_depth < 5:             # 영화에서 꿈 속에 꿈 속에 꿈 속에 꿈까지 4번 가길래
        print('\t'*(dream_depth-1), end=' ')
        character_name = character_stack.pop()      # 캐릭터를 뽑아서
        character_line(character_name)              # 대사 출력
        dream_depth += 1                            # 꿈 한 번 더 꾸기
        into_dream()                                # *** 재귀 포인트

    dream_depth -= 1                                # 꿈에서 빠져나오는 중
    print('\t'*(dream_depth-1), dream_depth, '에서 빠져나오는 중...')


visited = {}                # 피셔를 만났는지 저장할 변수
visited['피셔'] = False     # 아직 만나지 않음으로 초기화
characters = ['피셔', '맬', '사이토', '아서', '임스', '방해꾼1', '방해꾼2']     # 각 꿈 중 만나는 인물

print(' 피셔를 찾으러 가볼까?')
print()
tc = 0                      # 몇 번의 시도 만에 피셔를 만날 수 있을까요?
while not visited['피셔']:
    print(' --------------{} 번째 시도--------------'.format(tc+1))
    selected = []           # n 번째 시도에서 동일 인물을 중복해서 만나지 않기 위한 변수
    character_stack = []    # 꿈을 재귀로 접근하기 때문에 만나는 캐릭터를 담을 스택
    kick = dead = False     # 기존에 kick이나 dead를 False로 초기화
    dream_depth = 1         # 꿈의 깊이
    into_dream()            # 꿈으로 들어갑니다
    print()
    time.sleep(1)
    tc += 1

print(' {} 번 만에 임무를 성공했군...!'.format(tc))