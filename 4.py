def getNext(pole, inow, jnow):
    try:
        n = pole[inow][jnow]
    except IndexError:
        n = 1
    return n

pole = [0] * 15
for i in range(15):
    pole[i] = [0] * 8

pole[1][0] = 1
pole[2][0] = 1
pole[7][0] = 1
pole[14][0] = 1

pole[2][1] = 1
pole[7][1] = 1
pole[14][1] = 1

pole[2][2] = 1
pole[5][2] = 1
pole[6][2] = 1
pole[7][2] = 1
pole[8][2] = 1
pole[9][2] = 1
pole[12][2] = 1

pole[1][3] = 1
pole[2][3] = 1
pole[12][3] = 1

pole[2][4] = 1
pole[6][4] = 1
pole[7][4] = 1
pole[9][4] = 1
pole[10][4] = 1
pole[11][4] = 1
pole[12][4] = 1
pole[13][4] = 1

pole[6][5] = 1
pole[7][5] = 1
pole[11][5] = 1

pole[1][6] = 1
pole[4][6] = 1
pole[6][6] = 1
pole[6][6] = 1
pole[11][6] = 1

pole[1][7] = 1
pole[6][7] = 1
pole[7][7] = 1
pole[11][7] = 1


count = 0
for i in range(15):
    for j in range(8):
        if pole[i][j] == 1:
            continue
        inow = i
        jnow = j
        while getNext(pole, inow, jnow - 1) != 1:
            jnow -= 1
        while getNext(pole, inow + 1, jnow) != 1:
            inow += 1
        if getNext(pole, inow, jnow - 1) == 0 and getNext(pole, inow + 1, jnow - 1) == 0:
            count += 1

print(count)