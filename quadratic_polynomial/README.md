# Modular Arithmetic and Square Roots

This Python script provides functions for modular arithmetic and finding square roots modulo a prime, a power of a prime, or a polynomial.

## Functions:

### 1. `inv(num, mod)`

Calculates the modular inverse of a number.

### 2. `mod(num, mod)`

Performs modular arithmetic ensuring a non-negative result.

### 3. `square_prime(y, p)`

Finds square roots modulo a prime.

### 4. `power_gcd(y, p, n)`

Finds the power of a prime in the factorization of a number.

### 5. `square_power_prime(y, p, n)`

Finds square roots modulo a power of a prime.

### 6. `sqr(y, p, n)`

Finds square roots modulo a power of a prime recursively.

### 7. `crt(nums, lst)`

Performs the Chinese Remainder Theorem (CRT).

### 8. `sqr_poly(coef, modP)`

Finds square roots modulo a polynomial.

## Example Usage:

```python
# Example 1: Find square roots modulo a power of a prime
result = sqr(22, 3, 3)
print(result)

# Example 2: Perform Chinese Remainder Theorem (CRT)
nums = [a, b, c]
lst = [p1, p2, p3]
crt_result = crt(nums, lst)
print(crt_result)

# Example 3: Find square roots modulo a polynomial
poly_result = sqr_poly([3, 4, 5], [(3, 2), (5, 1)])
print(poly_result)
