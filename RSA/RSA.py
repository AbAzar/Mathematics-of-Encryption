import hashlib
import math
import os
import random

# Function to check if a number is prime
def is_prime(pNum):
    for i in range(2, int(math.sqrt(pNum)) + 1):
        if pNum % i == 0:
            return False
    return True


# Function to calculate the modular inverse
def inv(num, mod):
    for i in range(1, mod):
        if i * num % mod == 1:
            return i
    return False

# Function to perform modular arithmetic ensuring non-negative result
def mod(num, mod):
    if num >= mod:
        num = num % mod
    while num < 0:
        num = num + mod
    return num

# Function to calculate the MD5 hash of a file
def hashf(filename):
    f = open(filename, 'rb')
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

# Function to generate RSA keys
def generate_key():
    a = []
    while len(a) != 2:
        p = random.choice(primes)
        if p not in a:
            a.append(p)
    phi = (a[0] - 1) * (a[1] - 1)
    n = (a[0]) * (a[1])

    e = random.randint(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = inv(e, phi)
    while e == d:
        while math.gcd(e, phi) != 1:
            e = random.randint(1, phi)
        d = inv(e, phi)
    return n, e, d

# Function to encrypt a file using RSA
def encrypt():
    num = 1
    while True:

        plain = f.read(8)
        if len(plain) == 0 and num != 1:
            num = num * 2 + 1
            while num < n:
                num = 2 * num
            num -= n
            cipher = mod(num ** e, n)
            num = 1

            out.write(cipher.to_bytes(4, byteorder='big'))

        if len(plain) == 0:
            break

        for byte in plain:
            for i in range(7, -1, -1):
                bit = (byte >> i) & 1
                num *= 2
                num += bit
                if num >= n:
                    num -= n
                    cipher = mod(num ** e, n)
                    num = 1
                    out.write(cipher.to_bytes(4, byteorder='big'))
    myhash = hashf("file.txt")
    myhashByte = bytes(myhash, 'utf-8')
    num = 1
    for byte in myhashByte:
        for i in range(7, -1, -1):
            bit = (byte >> i) & 1
            num *= 2
            num += bit
            if num >= m:
                num -= m
                myhashByte = mod(num ** a, m)
                num = 1
                out.write(myhashByte.to_bytes(4, byteorder='big'))
    if num < m:
        num = num * 2 + 1
        while num < m:
            num = 2 * num
        num -= m
        myhashByte = mod(num ** a, m)
        num = 1

        out.write(myhashByte.to_bytes(4, byteorder='big'))
    f.close()
    out.close()
    return n, e, d

# Function to convert an integer to binary
def to_binary(plain):
    stg = ''
    while plain != 1:
        if plain % 2 == 0:
            stg = '0' + stg
        else:
            stg = '1' + stg
        plain = plain // 2
    return stg

# Function to decrypt a file encrypted with RSA
def decrypt():
    mid = open("midFile.txt", "rb")
    final = open("finalFile.txt", "wb")
    fsize = mid.read(4)
    fsize = int.from_bytes(fsize, byteorder='big')
    outD = ''
    endFlag = 0
    while True:
        cipher = mid.read(4)

        if len(cipher) == 0:
            break
        intCipher = int.from_bytes(cipher, byteorder='big')
        plain = mod(intCipher ** d, n)
        plain += n
        outD += to_binary(plain)
        while len(outD) >= 8:
            intData = int(outD[0:8], 2)
            final.write(intData.to_bytes(1, byteorder='big'))
            fsize -= 1
            outD = outD[8:]
            if fsize == 0:
                endFlag = 1
        if endFlag == 1:
            break
    final.close()
    myhash = hashf("finalFile.txt")
    orgHash = b''
    hashSize = 32
    outD = ""
    while True:
        cipher = mid.read(4)

        if len(cipher) == 0:
            break
        intCipher = int.from_bytes(cipher, byteorder='big')
        plain = mod(intCipher ** b, m)
        plain += m
        outD += to_binary(plain)
        while len(outD) >= 8 and hashSize != 0:
            intData = int(outD[0:8], 2)
            orgHash += intData.to_bytes(1, byteorder='big')
            hashSize -= 1
            outD = outD[8:]
    mid.close()
    orgHash = orgHash.decode('utf-8')
    if orgHash == myhash:
        return True
    else:
        return False

# Function to find RSA private key using the public key
def findKey(n, d):
    b = int(math.sqrt(n)) + 1
    c = (b ** 2) - n
    while int(math.sqrt(c)) ** 2 != c:
        b += 1
        c = b ** 2 - n
    res = int(math.sqrt(c))
    p = b - res
    q = b + res
    phi = (p - 1) * (q - 1)
    e = inv(d, phi)
    return n, e

# Example usage
f = open("file.txt", "rb")
fsize = os.path.getsize("file.txt")
out = open("midFile.txt", "wb")
out.write(fsize.to_bytes(4, byteorder='big'))
primes = [i for i in range(3, 100) if is_prime(i)]
n, e, d = generate_key()
m, a, b = generate_key()
print(n, e, d)
encrypt()
print(decrypt())
print(findKey(n, d))
