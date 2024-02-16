import secrets
from cryptography.fernet import Fernet


def generate_token(num_bytes: int = 32) -> str:
    """
    This function generates a random string.
    The num_bytes parameter specifies the number of random bytes to generate before the encoding to a string using Base64 encoding.
    Because of this encoding, the length of the resulting string is approximately 1.3x larger than the num_bytes specified.

    Parameters:
    num_bytes (int): The number of random bytes to generate before encoding. Default is 32.

    Returns:
    str: A random string.

    Example:
    >>> generate_token(num_bytes=16)
    '4LYAecdQvqH_W2OABLsZzV-6-zAAkt23'
    """

    token: str = secrets.token_urlsafe(nbytes=num_bytes)
    return token


def generate_secret_key() -> str:
    """
    This function generates a secret key that is compatible with the encrypt and decrypt functions.
    The generated secret key is suitable for the Fernet symmetric encryption algorithm,
    which this library uses for encryption.

    Returns:
    str: A secret key that can be used with the encrypt and decrypt functions.

    Example:
    >>> generate_secret_key()
    'gAAAAABgTD0yR3O4hV7Kb7PZ6N4iZA3uJNeL3_ZI2QmGJHbLZUj4Cy5B2Pgh4lX3JNLUZ4Q8OvJZ8OZyXUYd8l4XQJZIV64nJA=='
    """
    secret_key: str = Fernet.generate_key().decode()
    return secret_key
