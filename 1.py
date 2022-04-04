def getNext(pole, inow, jnow):
    try:
        n = pole[inow][jnow]
    except IndexError:
        n = 1
    return n

pole = [0] * 8
for i in range(8):
    pole[i] = [0] * 15

pole[0][10] = 1
pole[1][10] = 1
pole[2][10] = 1
pole[3][1] = 1
pole[4][1] = 1
pole[5][1] = 1
pole[5][2] = 1
pole[2][2] = 1
pole[2][3] = 1
pole[2][4] = 1
pole[2][5] = 1
pole[2][6] = 1
pole[2][7] = 1
pole[3][8] = 1
pole[6][3] = 1
pole[7][3] = 1
pole[6][4] = 1
pole[7][4] = 1
pole[6][7] = 1
pole[7][7] = 1
pole[6][8] = 1
pole[7][8] = 1
pole[5][9] = 1
pole[5][10] = 1
pole[2][12] = 1
pole[3][12] = 1
pole[4][12] = 1
pole[5][12] = 1

count = 0
for i in range(8):
    for j in range(15):
        if pole[i][j] == 1:
            continue
        inow = i
        jnow = j
        while getNext(pole, inow + 1, jnow) != 1:
            inow += 1
        while getNext(pole, inow, jnow + 1) != 1:
            jnow += 1
        if getNext(pole, inow - 1, jnow) == 0 and getNext(pole, inow - 1, jnow + 1) == 0:
            count += 1

print(count)