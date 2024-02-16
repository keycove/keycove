from .utils import _validate_type
import hashlib


def hash(plaintext: str) -> str:
    """
    This function hashes a given string using the SHA256 algorithm.

    Parameters:
    plaintext (str): The string to hash.

    Returns:
    str: The hashed string.

    Example:
    >>> hash("Hello, World!")
    '2ef7bde608ce5404e97d5f042f95f89f1c232871'
    """

    _validate_type(value=plaintext, arg_name="plaintext", expected_type=str)

    hashed_value: str = hashlib.sha256(plaintext.encode()).hexdigest()
    return hashed_value
