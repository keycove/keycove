from .utils import _validate_type
import hashlib
from cryptography.fernet import Fernet


def hash(value_to_hash: str) -> str:
    """
    This function hashes a given string using the SHA256 algorithm.

    Parameters:
    value_to_hash (str): The string to hash.

    Returns:
    str: The hashed string.

    Example:
    >>> hash("Hello, World!")
    '2ef7bde608ce5404e97d5f042f95f89f1c232871'
    """

    _validate_type(value=value_to_hash, arg_name="plaintext", expected_type=str)

    hashed_value: str = hashlib.sha256(value_to_hash.encode()).hexdigest()
    return hashed_value


def encrypt(value_to_encrypt: str, secret_key: str) -> str:
    """
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
    TypeError: If plaintext is not a string.

    Example:
    >>> secret_key = generate_secret_key()
    >>> encrypt("Hello, World!", secret_key)
    'gAAAAABgTD0yR3O4hV7Kb7PZ6N4iZA3uJNeL3_ZI2QmGJHbLZUj4Cy5B2Pgh4lX3JNLUZ4Q8OvJZ8OZyXUYd8l4XQJZIV64nJA=='
    """

    _validate_type(value_to_encrypt, "value_to_encrypt", str)
    _validate_type(secret_key, "secret_key", str)

    fernet_secret_key: Fernet = Fernet(secret_key.encode())
    encrypted_value: str = fernet_secret_key.encrypt(
        str.encode(value_to_encrypt)
    ).decode()
    return encrypted_value


def decrypt(encrypted_value: str, secret_key: str) -> str:
    """
    This function decrypts a given encrypted string using a provided secret key.
    The same secret key that was used to encrypt the encrypted_value should be used to decrypt it.

    Parameters:
    encrypted_value (str): The encrypted string to decrypt.
    secret_key (str): The secret key to use for decryption.

    Returns:
    str: The decrypted string.

    Raises:
    TypeError: If encrypted_value is not a string.

    Example:
    >>> secret_key = generate_secret_key()
    >>> encrypted_value = encrypt("Hello, World!", secret_key)
    >>> decrypt(encrypted_value, secret_key)
    'Hello, World!'
    """

    _validate_type(encrypted_value, "encrypted_value", str)
    _validate_type(secret_key, "secret_key", str)

    fernet_secret_key: Fernet = Fernet(secret_key.encode())
    decrypted_string: str = fernet_secret_key.decrypt(encrypted_value).decode()
    return decrypted_string
