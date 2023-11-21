# Mathematical Encryption Repository

This repository contains Python scripts showcasing various mathematical encryption and decryption algorithms. Each subproject serves a different purpose and demonstrates specific cryptographic techniques. Below is an overview of each subproject and its functionalities.

## 1. Polynomial Encryption and Decryption

### Overview

This Python script demonstrates a simple polynomial-based encryption and decryption algorithm using modular arithmetic.

### Usage

1. Run the `encrypt()` function to encrypt a file named "file.txt" and generate the encrypted file "out.txt".
2. Run the `decrypt()` function to decrypt the "out.txt" file and create the final decrypted file "final.txt".
3. The encryption key is generated and saved in the "key.txt" file.

## 2. Chinese Remainder Theorem (CRT) Encryption and Decryption

### Overview

This Python script demonstrates file encryption and decryption using the Chinese Remainder Theorem (CRT) based on prime numbers.

### Usage

1. Run the `encrypt()` function to encrypt a file named "file.txt" and generate the encrypted file "out.txt".
2. Run the `decrypt()` function to decrypt the "out.txt" file and create the final decrypted file "final.txt".

## 3. Modular Arithmetic and Square Roots

### Overview

This Python script provides functions for modular arithmetic and finding square roots modulo a prime, a power of a prime, or a polynomial.

### Example Usage

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
```

## 4. RSA Encryption and Decryption
### Overview
This Python script implements RSA encryption and decryption, including key generation and file hashing.
## Example Usage:

```python
# Example 1: Generate RSA keys and encrypt/decrypt a file
n, e, d = generate_key()
m, a, b = generate_key()
print(n, e, d)
encrypt()
print(decrypt())
print(findKey(n, d))
```