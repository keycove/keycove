import pytest
from keycove import hash, encrypt, decrypt, generate_secret_key


def test_hash_correct():
    plaintext = "Hello, World!"
    hashed_value = hash(plaintext)
    assert hashed_value != plaintext
    assert isinstance(hashed_value, str)


def test_hash_value_to_hash_incorrect_type():
    with pytest.raises(TypeError):
        hash(123)


def test_encrypt_correct():
    secret_key = generate_secret_key()
    value_to_encrypt = "Hello, World!"
    encrypted_value = encrypt(value_to_encrypt, secret_key)
    assert encrypted_value != value_to_encrypt
    assert isinstance(encrypted_value, str)


def test_encrypt_value_not_string():
    with pytest.raises(TypeError):
        encrypt(123, generate_secret_key())


def test_encrypt_incorrect_secret_key():
    secret_key = "abc"
    value_to_encrypt = "Hello, World!"
    with pytest.raises(ValueError):
        encrypt(value_to_encrypt, secret_key)


def test_encrypt_secret_key_not_string():
    with pytest.raises(TypeError):
        encrypt("Hello, World!", 123)


def test_decrypt_correct():
    secret_key = generate_secret_key()
    value_to_encrypt = "Hello, World!"
    encrypted_value = encrypt(value_to_encrypt, secret_key)
    decrypted_value = decrypt(encrypted_value, secret_key)
    assert decrypted_value == value_to_encrypt
    assert isinstance(decrypted_value, str)


def test_decrypt_encrypted_value_not_string():
    with pytest.raises(TypeError):
        decrypt(123, generate_secret_key())


def test_decrypt_incorrect_secret_key():
    secret_key = "qwerty"
    encrypted_value = "abc"
    with pytest.raises(ValueError):
        decrypt(encrypted_value, secret_key)


def test_decrypt_secret_key_not_string():
    secret_key = 123
    encrypted_value = "abc"
    with pytest.raises(TypeError):
        decrypt(encrypted_value, secret_key)
