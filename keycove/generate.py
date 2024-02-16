import secrets


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
