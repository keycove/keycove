from typing import Any


def _validate_type(value: Any, arg_name: str, expected_type: type) -> None:
    """
    This function checks if the provided value is a string.
    If the value is not a string, it raises a TypeError.

    Parameters:
    value (Any): The value to be type-checked.
    arg_name (str): The name of the argument being checked.
    expected_type (type): The expected type of the argument.

    Raises:
    TypeError: If the provided value is not the same type as the expected value.

    Example:
    >>> validate_type("Hello, World!", plaintext, str)  # No output, as "Hello, World!" is a string
    >>> validate_type(123, plaintext, str)
    TypeError: plaintext must be type str. int was provided
    """

    if not isinstance(value, expected_type):
        raise TypeError(
            f"{arg_name} must be type {expected_type.__name__}. {type(value).__name__} was provided"
        )
