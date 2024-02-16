import pytest
from keycove.utils import _validate_type


def test_validate_type_correct():
    _validate_type("Hello, World!", "plaintext", str)


def test_validate_type_incorrect_type():
    with pytest.raises(TypeError):
        _validate_type(123, "plaintext", str)
