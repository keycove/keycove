import pytest
from keycove import hash


def test_hash_correct():
    plaintext = "Hello, World!"
    hashed_value = hash(plaintext)
    assert hashed_value != plaintext
    assert isinstance(hashed_value, str)


def test_hash_value_to_hash_incorrect_type():
    with pytest.raises(TypeError):
        hash(123)
