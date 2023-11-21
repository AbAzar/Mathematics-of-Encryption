import math
import os
import random

lst = []
rng = input("number of prime :")


def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


primes = [i for i in range(3, 100) if isPrime(i)]
while len(lst) != int(rng):
    p = random.choice(primes)
    if p not in lst:
        lst.append(p)


def encrypt():
    f = open("file.txt", "rb")
    fsize = os.path.getsize("file.txt")

    out = open("out.txt", "wb")
    out.write(fsize.to_bytes(4, byteorder='big'))
    num = 1
    n = 1
    for p in lst:
        n *= p
    while True:
        byte = f.read(1)
        if len(byte) == 0 and num < n:
            num = num * 2 + 1
            while num < n:
                num = 2 * num
            num -= n
            for p in lst:
                out.write((num % p).to_bytes(1, byteorder='big'))
            break
        for i in range(7, -1, -1):
            bit = (byte[0] >> i) & 1
            num *= 2
            num += bit
            if num >= n:
                num -= n
                for p in lst:
                    out.write((num % p).to_bytes(1, byteorder='big'))
                num = 1

    f.close()
    out.close()


def inv(num, mod):
    for i in range(1, mod):
        if i * num % mod == 1:
            return i
    return False


def toBinary(res):
    stg = ''
    while res != 1:
        if res % 2 == 0:
            stg = '0' + stg
        else:
            stg = '1' + stg
        res = res // 2
    return stg


def crt(nums, lst):
    sumcrt = 0
    for i in range(len(nums)):
        M = 1
        for p in lst:
            M = (p * M)
        M = M // lst[i]
        sumcrt += nums[i] * M * inv(M, lst[i])
    M = 1
    for p in lst:
        M *= p
    return sumcrt % M


def decrypt():
    f = open("out.txt", "rb")
    final = open("final.txt", "wb")
    fsize = f.read(4)
    fsize = int.from_bytes(fsize, byteorder='big')
    outData = ''
    n = 1
    nums = []
    for p in lst:
        n *= p
    while True:
        num = f.read(len(lst))
        if len(num) == 0:
            break

        for i in range(len(lst)):
            nums.append(int(num[i]))

        res = crt(nums, lst)
        nums = []
        res += n
        outData += toBinary(res)
        while len(outData) >= 8 and fsize != 0:
            intData = int(outData[0:8], 2)
            final.write(intData.to_bytes(1, byteorder='big'))
            fsize -= 1

            outData = outData[8:]


encrypt()
decrypt()
