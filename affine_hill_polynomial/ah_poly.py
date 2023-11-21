import random
# Modulus for arithmetic operations
m = 17

# Function to compute the inverse of a polynomial modulo another polynomial
def inverse(poly, mod):
    def extended(p1, p2):
        if p2 == []:
            if p1[0][0] > 0:
                return False
            return [(0, 1)], p2
        a, b = extended(p2, divpoly(p1, p2)[1])
        q = divpoly(p1, p2)[0]
        return b, substc(a, mulpoly(b, q))

    res = extended(mod, poly)
    if not res:
        return False
    return inv(gcd(mod, poly)[0][1], m) * res[1]

# Function to compute the greatest common divisor of two polynomials
def gcd(p1, p2):
    if p2 == []:
        return p1
    return gcd(p2, divpoly(p1, p2)[1])

# Function to perform modular arithmetic on a number
def mod(num, mod):
    if num >= mod:
        num = num % mod
    while num < 0:
        num = num + mod
    return num

# Function to add a term to a polynomial
def addTerm(term, poly):
    if term[1] == 0:
        return poly
    if poly == []:
        return [term]
    if term[0] > poly[0][0]:
        return [term] + poly
    if term[0] < poly[0][0]:
        return [poly[0]] + addTerm(term, poly[1:])
    c = mod((term[1] + poly[0][1]), m)
    if c == 0:
        return poly[1:]
    return [(term[0], c)] + poly[1:]


##############################################################
def addPoly(poly1, poly2):
    if poly1 == []:
        return poly2
    if poly2 == []:
        return poly1
    return addPoly(poly1[1:], addTerm(poly1[0], poly2))


##############################################################
def negPoly(poly):
    return [(deg, mod(-coef, m)) for (deg, coef) in poly]


##############################################################
def mul(term1, term2):
    return (term1[0] + term2[0], mod(term1[1] * term2[1], m))


###############################################################
def mulTerm(term, poly):
    return [mul(term, t) for t in poly]


##############################################################
def mulpoly(poly1, poly2):
    if poly1 == []:
        return []
    if poly2 == []:
        return []
    return addPoly(mulTerm(poly1[0], poly2), mulpoly(poly1[1:], poly2))


#################################################################
def substc(poly1, poly2):
    return addPoly(poly1, negPoly(poly2))


def divpoly(dividend, divisor, qoutient=[]):
    if dividend == []:
        return qoutient, dividend
    if dividend[0][0] < divisor[0][0]:
        return qoutient, dividend
    deg = dividend[0][0] - divisor[0][0]
    coef = mod(dividend[0][1] * inv(divisor[0][1], m), m)
    term = (deg, coef)
    return divpoly(substc(dividend, mulTerm(term, divisor)), divisor, addTerm(term, qoutient))


def inv(num, mod):
    for i in range(1, mod):
        if i * num % mod == 1:
            return i
    return False


def mulmat(m1, m2):
    res = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            s = 0
            for k in range(len(m1[0])):
                s += mod(m1[i][k] * m2[k][j], m)
            res[i][j] = mod(s, m)
    return res


def addMat(m1, m2):
    res = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] = mod(m1[i][j] + m2[i][j], m)
    return res


def subMat(m1, m2):
    res = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] = mod(m1[i][j] - m2[i][j], m)
    return res


def invMat(matrix):
    def swapRows(mat, i, j):
        tmp = mat[i][:]
        mat[i] = mat[j][:]
        mat[j] = tmp

    mat = [[x for x in row] for row in matrix]
    size = len(mat)
    iMat = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                iMat[i][j] = 1
    for i in reversed(range(1, size)):
        if mat[i - 1][0] < mat[i][0]:
            swapRows(mat, i - 1, i)
            swapRows(iMat, i - 1, i)

    for i in range(size):
        for j in range(size):
            if i != j:
                # fixme : in modular case, item(i, i) may has no inverse
                if mat[i][i] == 0:
                    pivotFalg = 0
                    for r in range(i, size):
                        if mat[r][i] != 0:
                            swapRows(mat, i, r)
                            swapRows(iMat, i, r)
                            pivotFalg = 1
                    if pivotFalg == 0:
                        return False
                #
                tmp = mod(mat[j][i] * inv(mat[i][i], m), m)
                for k in range(size):
                    value = mod(mat[j][k] - mat[i][k] * tmp, m)
                    mat[j][k] = value
                    value = mod(iMat[j][k] - iMat[i][k] * tmp, m)
                    iMat[j][k] = value

    for i in range(size):
        tmp = mat[i][i]
        for j in range(size):
            mat[i][j] = mod(mat[i][j] * inv(tmp, m), m)
            iMat[i][j] = mod(iMat[i][j] * inv(tmp, m), m)

    return iMat


# key
blockSize = random.randint(3, 6)
#######
hMat = []
hMat = [[random.randint(0, m - 1) for i in range(blockSize)] for j in range(blockSize)]
while invMat(hMat) == False:
    hMat = [[random.randint(0, m - 1) for i in range(blockSize)] for j in range(blockSize)]
#######
bMat = [[random.randint(0, m - 1)] for i in range(blockSize)]
#######
polyMod = []
polyModLst = [(blockSize, random.randint(1, m - 1))] + [(i, random.randint(0, m - 1)) for i in range(blockSize)[::-1]]
for term in polyModLst:
    if term[1] != 0:
        polyMod.append(term)
#######
polyA = []
polyALst = [(i, random.randint(0, m - 1)) for i in range(blockSize)[::-1]]
for term in polyALst:
    if term[1] != 0:
        polyA.append(term)

while inverse(polyA, polyMod) == False:
    polyALst = [(i, random.randint(0, m - 1)) for i in range(blockSize)[::-1]]
    polyA = []
    for term in polyALst:
        if term[1] != 0:
            polyA.append(term)
#######
polyB = []
polyBLst = [(i, random.randint(0, m - 1)) for i in range(blockSize)[::-1]]
for term in polyBLst:
    if term[1] != 0:
        polyB.append(term)
#######
xorkey = bytes([random.randint(0, 255) for i in range(3, 9)])
#######
lst = []


def encrypt():
    f = open("file.txt", "rb")
    out = open("out.txt", "wb")
    while True:
        blk = f.read(len(xorkey))
        if len(blk) == 0:
            break
        for i in range(len(blk)):
            lst.append(blk[i] ^ xorkey[i])

    num = 1
    k = 0
    plainLst = []
    for byte in lst:
        for i in range(7, -1, -1):
            bit = (byte >> i) & 1
            num *= 2
            num += bit
            if num >= m:
                num -= m
                plainLst.append([num])
                num = 1
                k += 1
                if k == blockSize:
                    plainMat = plainLst
                    k = 0
                    plainLst = []
                    cMat = mulmat(hMat, plainMat)
                    cMat = addMat(cMat, bMat)
                    pPoly = []
                    for j in range(blockSize):
                        if cMat[j][0] == 0:
                            continue
                        pPoly.append((blockSize - j - 1, cMat[j][0]))
                    cPoly = divpoly(addPoly(mulpoly(polyA, pPoly), polyB), polyMod)[1]
                    outList = [0 for i in range(blockSize)]
                    for i in range(len(cPoly)):
                        outList[blockSize - cPoly[i][0] - 1] = cPoly[i][1]
                    for data in outList:
                        out.write(data.to_bytes(1, byteorder='big'))

    f.close()
    out.close()


encrypt()


def toBinary(res):
    stg = ''
    while res != 1:
        if res % 2 == 0:
            stg = '0' + stg
        else:
            stg = '1' + stg
        res = res // 2
    return stg


def decrypt():
    coef = []
    cPoly = []
    f = open("out.txt", "rb")
    final = open("final.txt", "wb")
    outData = ''
    xorKeyCnt = 0
    while True:
        num = f.read(blockSize)
        if len(num) == 0:
            break

        for i in range(blockSize):
            coef.append(int(num[i]))

        for i in range(len(coef)):
            if coef[i] != 0:
                cPoly.append((blockSize - i - 1, coef[i]))
        pPoly = divpoly(mulpoly(substc(cPoly, polyB), inverse(polyA, polyMod)), polyMod)[1]
        cipherList = [[0] for i in range(blockSize)]
        for i in range(len(pPoly)):
            cipherList[blockSize - pPoly[i][0] - 1] = [pPoly[i][1]]
        plainMat = mulmat(invMat(hMat), subMat(cipherList, bMat))
        for i in range(len(plainMat)):
            mah = plainMat[i][0] + m
            outData += toBinary(mah)
            while len(outData) >= 8:
                intData = int(outData[0:8], 2)
                final.write((intData.to_bytes(1, byteorder='big')[0] ^ xorkey[xorKeyCnt]).to_bytes(1, byteorder='big'))
                xorKeyCnt += 1
                xorKeyCnt %= len(xorkey)
                outData = outData[8:]
        cPoly = []
        coef = []

    f.close()
    final.close()


def writeKey():
    keyFile = open("key.txt", "wb")
    # write m
    keyFile.write(m.to_bytes(1, byteorder='big'))
    # write xorkey
    keyFile.write(len(xorkey).to_bytes(1, byteorder='big'))
    for byte in xorkey:
        keyFile.write(byte.to_bytes(1, byteorder='big'))
    # write blockSize
    keyFile.write(blockSize.to_bytes(1, byteorder='big'))
    # write hMat
    for i in range(blockSize):
        for j in range(blockSize):
            keyFile.write(hMat[i][j].to_bytes(1, byteorder='big'))
    # write bMat
    for i in range(blockSize):
        keyFile.write(hMat[i][0].to_bytes(1, byteorder='big'))

    # write polyMod
    polyList = [0 for i in range(blockSize + 1)]
    for i in range(len(polyMod)):
        polyList[blockSize - polyMod[i][0]] = polyMod[i][1]
    for i in polyList:
        keyFile.write(i.to_bytes(1, byteorder='big'))

    # write polyA
    polyList = [0 for i in range(blockSize)]
    for i in range(len(polyA)):
        polyList[blockSize - polyA[i][0] - 1] = polyA[i][1]
    for i in polyList:
        keyFile.write(i.to_bytes(1, byteorder='big'))

    # write polyB
    polyList = [0 for i in range(blockSize)]
    for i in range(len(polyB)):
        polyList[blockSize - polyB[i][0] - 1] = polyB[i][1]
    for i in polyList:
        keyFile.write(i.to_bytes(1, byteorder='big'))

    keyFile.close()


writeKey()
decrypt()
