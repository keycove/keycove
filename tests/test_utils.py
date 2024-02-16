import pytest
from keycove import validate_type


def test_validate_type_correct():
    validate_type("Hello, World!", "plaintext", str)


def test_validate_type_incorrect_type():
    with pytest.raises(TypeError):
        validate_type(123, "plaintext", str)
