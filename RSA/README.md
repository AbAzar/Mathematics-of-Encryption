# RSA Encryption and Decryption

This Python script implements RSA encryption and decryption, including key generation and file hashing.

## Functions:

### 1. `is_prime(pNum)`

Checks if a number is prime.

### 2. `inv(num, mod)`

Calculates the modular inverse of a number.

### 3. `mod(num, mod)`

Performs modular arithmetic ensuring a non-negative result.

### 4. `hashf(filename)`

Calculates the MD5 hash of a file.

### 5. `generate_key()`

Generates RSA public and private keys.

### 6. `encrypt()`

Encrypts a file using RSA.

### 7. `to_binary(plain)`

Converts an integer to binary.

### 8. `decrypt()`

Decrypts a file encrypted with RSA and verifies the integrity using file hashing.

### 9. `findKey(n, d)`

Finds the RSA private key using the public key.

## Example Usage:

```python
# Example 1: Generate RSA keys and encrypt/decrypt a file
n, e, d = generate_key()
m, a, b = generate_key()
print(n, e, d)
encrypt()
print(decrypt())
print(findKey(n, d))
