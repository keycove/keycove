import pytest
from keycove import generate_token


def test_generate_token_correct():
    api_key = generate_token()
    assert len(api_key) == 43
    assert isinstance(api_key, str)


def test_generate_token_incorrect_type():
    with pytest.raises(TypeError):
        api_key = generate_token("thirty")
