# Polynomial Encryption and Decryption

This Python script demonstrates a simple polynomial-based encryption and decryption algorithm using modular arithmetic.

## Usage

1. Run the `encrypt()` function to encrypt a file named "file.txt" and generate the encrypted file "out.txt".
2. Run the `decrypt()` function to decrypt the "out.txt" file and create the final decrypted file "final.txt".
3. The encryption key is generated and saved in the "key.txt" file.

## Key Generation

The key includes the following components:
- `m`: Modulus for polynomial operations.
- `xorkey`: XOR key used for bitwise encryption.
- `blockSize`: Size of the polynomial blocks.
- `hMat`: Matrix used for polynomial multiplication.
- `bMat`: Matrix used in polynomial addition.
- `polyMod`: Modulus polynomial for encryption.
- `polyA` and `polyB`: Polynomials used in encryption and decryption.

## File Structure

- `file.txt`: Input file for encryption.
- `out.txt`: Encrypted file.
- `final.txt`: Decrypted final output.
- `key.txt`: Key file containing encryption parameters.
