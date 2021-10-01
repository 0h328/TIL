amho = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
line = '1100101000110100011010111101101110010011001001101110110000000000000000000000000000000110010110111010111100010110100011000101101100010101111'


def amho_avail(data, scale):
    data = data[:: scale]
    ret = []

    # 7개씩 끊어서 체크하기
    # 반복문 진행하면서 만약에 암호체크가안되면 return 0
    # 암호체크되면 ret 에 넣기

    return tuple(ret)


scale = 1
while line:
    line = line.zfill(56 * scale)
    hubo = line[-56 * scale:]
    ret = amho_avail(hubo, scale)
    if ret != 0:
        # ret <- 생성된 코드를 return 받아오면 된다
        # set() 에다가 추가해주기
        line = line[:-56 * scale].rstrip('0')
        scale = 1
    else:
        scale += 1