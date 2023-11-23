# DES Encryption and Decryption

This Python script implements the Data Encryption Standard (DES) algorithm for encryption and decryption. DES is a symmetric-key block cipher that operates on 64-bit blocks of data using a 56-bit key.

## Usage

### Prerequisites

Make sure to have Python installed on your system.

### Input Data

The script reads the input data from a file named "f.txt". Ensure that the file is present and contains the data to be encrypted.

```python
f = open("f.txt", "rb")
```
## Encryption

The script generates a random 64-bit key and encrypts the data using the DES algorithm.


```python
key = ''.join([str(random.randint(0, 1)) for i in range(64)])
print("Generated Key:", key)

c = encryptD()
print("Encrypted Data:", c)
```
## Decryption

To decrypt the data, the script uses the generated key and the DES algorithm.

```python
decryptD()
```
The decrypted data will be printed to the console.
Important Note

This script uses the pyDes library for DES encryption and decryption. Install the library before running the script:

```bash
pip install pyDes
```