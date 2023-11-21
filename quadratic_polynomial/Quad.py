import math

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

# Function to find square roots modulo a prime
def square_prime(y, p):
    def helper(g, y, q, qInv):
        if g % 4 == 2:
            return [(y ** ((g + 2) // 4)) % p, mod(-(y ** ((g + 2) // 4)), p)]
        if g % 4 == 0:
            if (y ** (g // 4)) % p == 1:
                return helper(g // 2, y, (q ** 2) % p, (inv(q, p) ** 2) % p)
            if (y ** (g // 4)) % p == p - 1:
                a, b = helper(g // 2, (y * q ** 2) % p, (q ** 2) % p, (inv(q, p) ** 2) % p)
                return (a * qInv) % p, (b * qInv) % p

    if (y ** ((p - 1) // 2) % p) == p - 1:
        return False
    elif (y ** ((p - 1) // 2) % p) == 1:
        q = 2
        for i in range(2, p):
            if (y ** ((p - 1) // 2) % p) == p - 1:
                q = i
                break
        return helper(p - 1, y, q, inv(q, p))
    return False


# Function to find the power of a prime in the factorization of a number
def power_gcd(y, p, n):
    cnt = 0
    for i in range(n):
        if mod(y, p) == 0:
            cnt += 1
            y = y // p
    return cnt

# Function to find square roots modulo a power of a prime
def square_power_prime(y, p, n):
    x = []
    if mod(y, p ** n) == 0:
        for i in range(0, p ** (n // 2)):
            x.append(mod(i * (p ** ((n // 2) + 1)), p))
            return x
    if mod(y, p ** n) != 0:
        res = power_gcd(y, p, n)
        if res % 2 != 0:
            return False
        elif res == 0:
            return sqr(y, p, n)
        elif res % 2 == 0:
            k = res // 2
            lst = sqr(y // p ** res, p, n - res)
            if lst == False:
                return False
            finRes = []
            for i in range(p ** k):
                for j in lst:
                    finRes.append(i * (p ** (n - k)) + (j * (p ** k)))
            return finRes

# Function to find square roots modulo a power of a prime
def sqr(y, p, n):
    if n == 1:
        return square_prime(y, p)
    res = sqr(mod(y, p ** (n - 1)), p, n - 1)
    if res == False:
        return False
    ansList = [(mod(mod(((y - (x ** 2)) // (p ** (n - 1))), p ** n) * inv(2, p) * inv(x, p), p), x) for x in res]
    return [mod((p ** (n - 1)) * alpha + x, p ** n) for alpha, x in ansList]


print(sqr(22, 3, 3))

# Function to perform Chinese Remainder Theorem (CRT)
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

# Function to find square roots modulo a polynomial
def sqr_poly(coef, modP):
    m = 1
    for i in modP:
        m *= (i[0] ** i[1])
    aGcd = math.gcd(coef[0], m)
    if aGcd == 1:
        aInv = inv(coef[0], m)
        for i in range(len(coef)):
            coef[i] = mod(coef[i] * aInv, m)
        B = 0
        if coef[1] % 2 == 0:
            B = mod(coef[1] // 2, m)
        else:
            B = mod(coef[1] * inv(2, m), m)
        Y = mod(B ** 2 - coef[2], m)
        res = []
        for powerPrime in modP:
            tmp = square_power_prime(mod(Y, powerPrime[0] ** powerPrime[1]), powerPrime[0], powerPrime[1])
            if not tmp:
                return False
            res.append(tmp)
        # [[1, 2], [3, 4]]
        crtRes = []
        if (len(res) > 1):
            factors = [modP[0][0] ** modP[0][1], modP[1][0] ** modP[1][1]]
            for i in range(len(res[1])):
                crtRes.append(crt([res[0][0], res[1][i]], factors))
        elif len(res) == 1:
            crtRes = res[0]
        else:
            return False
        # for over crt result
        ans = []
        for i in range(len(crtRes)):
            ans.append(mod(crtRes[i] - B, m))
            # ans.append(mod(-crtRes[i] - B, m))
        return ans
    else:
        bInv = inv(coef[1], aGcd)
        if bInv == False:
            return False
        alpha = mod(-coef[2] * bInv, aGcd)
        newCoef = [coef[0] * aGcd, (2 * coef[0] * alpha) + coef[1],
                   (coef[0] * alpha ** 2 + coef[1] * alpha + coef[2]) // aGcd]
        tmp = [[x, y] for x, y in modP]
        gcdTmp = aGcd
        for i in range(len(modP)):
            while gcdTmp % modP[i][0] == 0:
                tmp[i][1] -= 1
                gcdTmp /= modP[i][0]
        newMod = []
        for prime in tmp:
            if prime[1] != 0:
                newMod.append((prime[0], prime[1]))
        res = sqr_poly(newCoef, newMod)
        finRes = []
        for r in res:
            finRes.append(aGcd * r + alpha)
        return finRes

# Example usage
print(square_power_prime(63, 3, 4))
print(sqr_poly([3, 4, 5], [(3, 2), (5, 1)]))
print(sqr_poly([3, 4, 13], [(5, 1), (7, 1)]))
