# Keycove

An easy-to-use API key authorization library.

The key features are:

- **Generating tokens**: Generates random tokens that can be used as API keys.
- **Hashing**: Hash API keys to securely store them in your database.
- **Encryption / Decryption**: Encrypt API keys to securely store keys. Decrypt to view them again.

Generally, encryption / hashing algorithms work with bytes as inputs and outputs to these algorithms. Keycove takes care of converting values to / from bytes so you only need to work with strings.


## Generate a token

```python
generate_token(num_bytes: int = 32) -> str
```
This function generates a random string that can be uses as an API key.
The num_bytes parameter specifies the number of random bytes to generate before the encoding to a string using Base64 encoding.
Because of this encoding, the length of the resulting string is approximately 1.3x larger than the num_bytes specified.
 
Parameters:
num_bytes (int): The number of random bytes to generate before encoding. Default is 32.
 
Returns:
str: A random string.
 
Example:
```python
>>> from keycove import generate_token
>>> generate_token(num_bytes=16)
'4LYAecdQvqH_W2OABLsZzV-6-zAAkt23'
```


## Generate a secret key

```python
generate_secret_key() -> str
```
This function generates a secret key that is compatible with the encrypt and decrypt functions.
The generated secret key is suitable for the Fernet symmetric encryption algorithm, which this library uses for encryption.
 
Returns:
str: A secret key that can be used with the encrypt and decrypt functions.
 
Example:
```python
>>> from keycove import generate_secret_key
>>> generate_secret_key()
'gAAAAABgTD0yR3O4hV7Kb7PZ6N4iZA3uJNeL3_ZI2QmGJHbLZUj4Cy5B2Pgh4lX3JNLUZ4Q8OvJZ8OZyXUYd8l4XQJZIV64nJA=='
```


## Encrypt

```python
encrypt(value_to_encrypt: str, secret_key: str) -> str
```
This function encrypts a given string using a provided secret key.
Use keycove.generate_secret_key() to generate this secret key.
This secret key is suitable for the Fernet symmetric encryption algorithm,
which is used for encryption.
 
Parameters:
value_to_encrypt (str): The string to encrypt.
secret_key (str): The secret key to use for encryption.
Use keycove.generate_secret_key() to generate this secret key.
 
Returns:
str: The encrypted string.
 
Raises:
TypeError: If value_to_encrypt is not a string.
TypeError: If secret_key is not a string.
ValueError: If secret_key is incorrect.
 
Example:
```python
>>>from keycove import encrypt, generate_secret_key
>>> secret_key = generate_secret_key()
>>> encrypt(value_to_encrypt="Hello, World!", secret_key=secret_key)
'gAAAAABgTD0yR3O4hV7Kb7PZ6N4iZA3uJNeL3_ZI2QmGJHbLZUj4Cy5B2Pgh4lX3JNLUZ4Q8OvJZ8OZyXUYd8l4XQJZIV64nJA=='
```


## Decrypt

```python
decrypt(encrypted_value: str, secret_key: str) -> str
```
This function decrypts a given encrypted string using a provided secret key.
The same secret key that was used to encrypt the encrypted_value should be used to decrypt it.
 
Parameters:
encrypted_value (str): The encrypted string to decrypt.
secret_key (str): The secret key to use for decryption.
 
Returns:
str: The decrypted string.
 
Raises:
TypeError: If encrypted_value is not a string.
TypeError: If secret_key is not a string.
ValueError: If secret_key is incorrect.
 
Keycove is an easy-to-use API key authorization library.

Example:
```python
>>> from keycove import decrypt, encrypt, generate_secret_key
>>> secret_key = generate_secret_key()
>>> encrypted_value = encrypt(value_to_encrypt="Hello, World!", secret_key=secret_key)
>>> decrypt(encrypted_value=encrypted_value, secret_key=secret_key)
'Hello, World!'
```


## Hash

```python
hash(plaintext: str) -> str
```
This function hashes a given string using the SHA256 algorithm.
 
Parameters:
value_to_hash (str): The string to hash.
 
Returns:
str: The hashed string.
 
Example:
```python
>>>from keycove import hash
>>> hash(value_to_hash="Hello, World!")
'2ef7bde608ce5404e97d5f042f95f89f1c232871'
```